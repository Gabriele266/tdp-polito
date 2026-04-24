
# Cursor
E' la struttura che mi permette di interagire con il DBMS ed eseguire degli statement SQL sotto forma di stringa
E' un puntatore alla posizione nella tabella su cui sto operando nel server
Tipicamente parte dalla riga prima di quella che serve a me  
L'idea è che piazzo il puntatore in una posizione iniziale e poi gli dico di spostarlo per leggere fino al pezzo che mi serve. Il contenuto su cui vado a lavorare
è il result set di una query, ossia la tabella con i risultati della query SQL. 

## Creazione del cursore
La classe che utilizzo è la `MySQLCursor` tramite il metodo `cursor` della connection. Ci sono diverse classi che ereditano dalla classe base 
`Cursor` e mi permettono di ottenere i dati sotto forma di strutture dati diverse in python (dizionari, tuple). 
Per cambiare il tipo di cursore si passano argomenti diversi al metodo `cursor`. Se non specifico niente i risultati vengono fuori sotto forma di tupla. 
Il più comodo da utilizzare è il dizionario. 

## Utilizzo del cursore
```
query = """Select id, name from user"""
cursor.execute(query)
```

Creo una query sotto forma di stringa e la eseguo tramite il metodo `execute` del cursore, creato a sua volta dalla connessione. 
Dentro cursor troverò il result-set della mia query. Tipicamente il contenuto della query dipende da degli elementi dinamici che provengono 
dalla UI. Devo poterla modificare. 
Il metodo più semplice è **utilizzare l'interpolazione** delle stringhe ma non ci piace. Non è elegante. **Può subire SQL injection se non viene verificato prima**

## Parametric statement
**Parametric statements** --> Sono delle query che hanno dei parametri al loro interno di cui conosco il tipo. 
La libreria effettua controlli sui parametri passati, cercando delete strani o SQL Injection. 
Utilizzando i parametric statement viene **separata** la **creazione** della query dalla sua **esecuzione**. 
Inizialmente definisco il **template** della query con dei **placeholder** al posto dei valori, che verranno sostituiti dopo, eventualmente dopo controlli. 

Gli statement parametrici li posso riutilizzare più volte. 

## Prototipo di utilizzo in scrittura
```
cnx = connect(....)         # Effettuo la connessione al database
curs = cnx.cursor(....)     # Creo un cursore per operare sul database

query = """
INSERT INTO tests 
    (id, name, value) 
    VALUES (%s, %s, %s)     # Definisco una query parametrica in cui i %s rappresentano delle stringhe
"""         

cursor.execute(query, <valori>)       # Eseguo la query passando i valori specifici da sostituire ai diversi %s
cnx.commit()                           # Tutte le modifiche al database devono essere seguite da una commit, che termina la transazione e scrive effettivamente

cursor.close()                          # Sia il cursore che la connessione devono essere chiusi
cnx.close()
```

La query parametrica è sempre **una stringa con dei segnaposto**. Quando la eseguo dovrò sempre passare i valori effettivi **sotto forma di tupla**
I parametri **sono ordinati**. 

## Prototipo in lettura
```
cnx = connect(....)         # Effettuo la connessione al database
curs = cnx.cursor(....)     # Creo un cursore per operare sul database

query = """
SELECT * FROM tests"""         

cursor.execute(query, <valori>)       # Eseguo la query passando i valori specifici da sostituire ai diversi %s

for (id, name, value) in cursor:
    print(id, name, value)

cursor.close()                          # Sia il cursore che la connessione devono essere chiusi
cnx.close()
```
Nel cursore mi trovo il result-set, una tabella con il risultato della query. Quando effettuo una lettura avrò sempre un ciclo sul mio cursore
per esplorare i risultati. A seconda della struttura dati del cursore avrò modalità diverse
Il cursore viene utilizzato **come se fosse un iterable.** 
Nota: non mi serve più effettuare la `commit` perchè non ho modificato il DB. 
Quando è un dizionario, **ogni riga viene mappata come un dizionario diverso**

```
for row in cursor:
    print(row["id”])
    print(row["name”])
    print(row["value”])
```

## Metodi fetch
Per evitare di effettuare un'iterazione:
* `fetchone()` restituisce un solo risultato o none se non è presente. Posso ri-utilizzarla per leggere più righe una per volta
* `fetchmany(N)` restituisce N righe
* `fetchall()` restituisce tutte le righe che non ho ancora letto sotto forma di lista
La posizione del puntatore viene spostata ogni volta, influenzando i risultati delle query successive. 

Nota: se non leggo tutti i risultati mi viene dato un errore quando faccio la chiusura del cursore, questo succede se il cursore non è posizionato alla fine quando effettuo la chiusura. 
L'errore è `Unread result found` di tipo `InternalError`

## Conversione dei tipi
In automatico la libreria converte i tipi SQl in tipi Python