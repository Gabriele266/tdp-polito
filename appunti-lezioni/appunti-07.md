# DB

I DTO sono delle dataclass che hanno gil stessi campi della tabella nel database

Devono avere anche il metodo `__hash__` e il `__eq__`

## DAO
I DAO (Data access object) sono delle classi che contengono solo metodi per accedere al database e **restituiscono** delle istanze di DAO
Esso gestisce la connessione al database, effettua le query, gestisce eventuali eccezioni lanciate. 
Non hanno un proprio stato, a parte le informazioni sullo stato della connessione. Tipicamente utilizzano parametri di classe. 
I DAO offrono metodi CRUD per svolgere le operazioni. 
Di default i metodi del DAO sono **metodi statici**, non hanno bisogno di self

## DTO
```python
from dataclasses import dataclass

@dataclass
class ClienteRecord:
    nome: str
    email: str      # PK
    categoria: str

    def __hash__(self):
        return hash(self.email)     # Lo hash viene calcolato sempre a partire dalla chiave primaria

    def __eq__(self, other):
        return self.email == other.email        # il controllo viene fatto sulla PK
```

A ogni entità vado ad associare un oggetto DAO (per accedere alle info sul DB) e un oggetto DTO (per rappresentare l'entità presente sul DB)
StudentDAO (accede al db) --> StudentDTO (rappresenta uno studente nel db)

## Object Relational Mapping
E' un pattern di programmazione che permette di spostare dati dal db rimanendo indipendenti. 
Le relazioni tra tabelle (che in SQL vengono mappate con chiavi foreign) devono essere mappate in Python. 
La singola tabella è mappata dal DTO, togliendo le colonne FK. 
Per le tabelle utilizzate per memorizzare le relazioni, non si creano dei DTO. 
Per mappare le relazioni, si aggiungono campi al DTO (eventualmente con dei getter), in modo tale da poterle gestire comodamente. 

E' IMPORTANTE CAPIRE QUALI TABELLE SERVONO E QUALI COLONNE --> NON è NECESSARIO MAPPARE TUTTO SUL CODICE SE NON SERVE

NEL CASO IN CUI LA **PK SIA PIù DI UNA**, SI USA UNA **TUPLA**

## Connection pool
Ho un insieme di connessioni già aperte che utilizzo quando mi servono. All'avvio del programma apro più connessioni, 
quando mi servono ne richiedo una e poi la utilizzo. Una volta utilizzata, viene rimessa dentro. Questo perchè creare gli oggetti connect è costoso in termini
computazionali. 
MySQL connector ha il modulo **pooling**
Quando creo il pool devo specificarne la dimensione. 
Quando faccio una query, utilizzo la `<pool>.get_connection()` che mi restituisce una connessione utile. 
Per ogni database diverso creo un pool. Se la connessione è in un pool, la `close` non la chiude ma la rimette a disposizione nel pool. 

## Configurazione del DB
Per config si crea un file `connector.cfg` con i secret:

```
[client]
user=...
password=...
database=...
```
Nel connector le informazioni vengono caricate dal file cfg e non scritte direttamente nel codice. 
pathlib è utile per ottenere il percorso del file attuale che sta venendo eseguito e mi permette di navigare nelle cartelle. 
`"f{pathlib.Path(__file__).resolve().parent()}/connector.cfg"`
poi carico le configurazioni tramite l'opzione "option_files" del connector.