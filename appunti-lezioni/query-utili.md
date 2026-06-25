# Query utili

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