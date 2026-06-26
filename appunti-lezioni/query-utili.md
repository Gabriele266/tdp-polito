# Query utili

## Indicazioni generali
* FARE ATTENZIONE AI **NOMI DEI CAMPI SU CUI SI FA UNA JOIN**
* Costruire prima le query provandole con dati mock e verificando che i risultati portino a quelli negli output di esempio
* Se possibile, costruire una query che restituisca direttamente la **tabella degli edges** da aggiungere al grafo
* Se ragiono a coppie sul database, gli id devono essere uno più grande dell'altro (`>`) per evitare doppioni
* Prima strutturare la query singola, poi quella a coppie

Per il calcolo di statistiche aggregate è utile fare una JOIN con tutte le tabelle che hanno informazioni utili e realizzare
una tabella riassuntiva unica, che abbia abbastanza informazioni per calcolare tutte le statistiche di interesse.  

```sql
SELECT AL.ArtistId, INV.CustomerId, COUNT(*) as conteggio_track 
                FROM InvoiceLine IL, 
                     Invoice INV, 
                     Track T, 
                     Album AL, 
                     Genre GE, 
                     Artist A
                WHERE IL.InvoiceId = INV.InvoiceId 
                  AND IL.TrackId = T.TrackId 
                  AND T.GenreId = GE.GenreId 
                  AND T.AlbumId = AL.AlbumId 
                  AND GE.GenreId = %s 
                  AND AL.ArtistId = A.ArtistId
                GROUP BY AL.ArtistId, INV.CustomerId
                ;
```

Esempio di query con molte tabelle (tutte collegate tramite le WHERE) e un raggruppamento su 2 campi. 
Quando si applica una GROUP BY con 2 campi, viene realizzata una tabella in cui le coppie dei due campi sono univoche e nella terza colonna vengono calcolati i valori 
aggregati sulla coppia (che rappresenta il gruppo).   

## Query annidate

Posso utilizzare delle query annidate anche come campo aggiuntivo nella select. 
```sql
SELECT A2.ArtistId, A2.Name, 
       (SELECT COUNT(*) FROM Track T WHERE T.AlbumId IN (
	SELECT A.AlbumId FROM Album A, Artist AR WHERE A.ArtistId = A2.ArtistId 
) AND T.GenreId = %s) as numero_brani_genere 
FROM Artist A2;
```
In questo caso la query restituisce una tabella con 3 colonne, di cui l'ultima è calcolata facendo una sotto-query.  

## Filtri possibilmente null
Per gestire un insieme di filtri opzionali, è utile la funzione `COALESCE` di SQL, che restituisce il primo valore non-null di un insieme. 

```sql
SELECT COALESCE(NULL, "CIAO");
```

La posso inserire in condizioni per verificare un filtro nullabile, mettendo prima il valore del filtro e poi un valore placeholder (eventualmente anche il nome del campo)
```sql
SELECT * FROM TABLE WHERE campo=COALESCE(<filter-value>, campo);
```
In questo modo, se il filtro è popolato viene applicato, altrimenti si riduce ad un controllo a=a che sarà sempre vero. 

## Prendere tabelle a coppie e generare le combinazioni
Può essere utile dover prendere la stessa tabella a coppie. Ognuno dei due elementi cardine A e B viene joinato con tutte le informazioni necessarie per applicare i diversi filtri. 
Alla fine, si raggruppa per tutte le coppie univoche e si calcola un aggregato (in questo caso utilizzando diverse funzioni per convertirlo)
In questo caso una delle condizioni è che entrambe le tabelle cardine abbiano in comune lo stesso movie_id associato.  

```sql
# Considera tutte le coppie di autori nel database, prendendo tutte le informazioni di ognuno dei due
# Per ognuno dei due autori, prende le informazioni e i film che hanno fatto insieme (la condizione sull'id del film deve corrispo# Per evitare che vengano considerate coppie tra lo stesso autore o con ordine diverso, si utilizza il <
select rm1.name_id as Actor1, rm2.name_id as Actor2, sum( cast(replace(replace(m.worlwide_gross_income, '$', ''),',', '') as unsigned)) as Weight
        from movie m, role_mapping rm1, role_mapping rm2, ratings r, names n1, names n2
        where m.id = rm1.movie_id
        and m.id = rm2.movie_id
        and m.id = r.movie_id
        and rm1.name_id = n1.id
        and rm2.name_id = n2.id
        and n1.date_of_birth IS NOT NULL
        and n2.date_of_birth IS NOT NULL
        and rm1.name_id < rm2.name_id	# Per evitare di ri-prendere gli stessi attori o lo stesso attore due volte
        and r.avg_rating >= 6
        and r.avg_rating <= 7
        and m.worlwide_gross_income is not null
        and m.worlwide_gross_income like '$%'
        group by rm1.name_id, rm2.name_id		
  # prendo tutte le coppie di autori univoche
# La singola riga ha informazioni di due attori che hanno recitato nello stesso film
```

## Query con ricerca di righe la cui data sta in un range di date
```sql
SELECT oi.product_id, COUNT(*) as numero_vendite FROM order_items oi, orders o, products p
        WHERE oi.product_id = p.product_id AND
        oi.order_id = o.order_id AND 
        o.order_date BETWEEN %s AND %s
	    group by oi.product_id;
```

Le due date vengono fornite con la riga: 
```python
data = tuple([range_s, range_e])
```
e sono due istanze della classe `datetime` del modulo `datetime`. Non è necessario formattarle, ci pensa il db.  
Per convertirle in stringa usare `datetime.strptime(event.data, "%Y-%m-%dT%H:%M:%S.%f")` con il formato adatto (gli ultimi sono i millisecondi)

## Query prendendo a coppie i piloti
Questa query resituisce direttamente gli archi per il grafo. 
```sql
# A coppie di pilota, il numero di gare che hanno corso come compagni nel range selezionato, qualificandosi
# Prendo due piloti diversi con tutte le informazioni associate, guardo se sono compagni di squadra
# Devono avere lo stesso constructorId per essere compagni di squadra
SELECT REA.driverId as driver_a, REB.driverId as driver_b, COUNT(*) as weight
FROM results REA, drivers DVA, races RSA,
	results REB, drivers DVB, races RSB
	WHERE REA.raceId = RSA.raceId AND 
	REA.driverId = DVA.driverId AND
	REA.position IS NOT NULL	AND			# Deve essere arrivato
	RSA.year BETWEEN 2007 AND 2008	AND	# L'anno della gara deve essere nel range
	REB.raceId = RSB.raceId AND 
	REB.driverId = DVB.driverId AND
	REB.position IS NOT NULL	AND	# Deve essere arrivato
	RSB.year BETWEEN 2007 AND 2008 AND
	REA.driverId > REB.driverId AND		# A e B devono essere due piloti distinti, facendo in modo che non ci siano ripetizioni
	REA.raceId = REB.raceId AND			# I due piloti devono aver guidato nella stessa gara
	REA.constructorId = REB.constructorId 	# A e B devono avere lo stesso costruttore
	GROUP BY REA.driverId, REB.driverId;
```