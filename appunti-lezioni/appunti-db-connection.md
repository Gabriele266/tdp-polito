
# DataBase connection
DBMS --> Database management system, salva i dati e li recupera
Ci permette di interrogare il db
Supporto sia per MySQL che per MariaDB
Per interrogare il DB utilizziamo DBeaver, un'interfaccia grafica che ci permette di interagire con i db
* Modificare i dati --> Data Editor
* Esecuzione di query SQL --> SQL Editor per provarle (prima di eseguirle nel codice)
* Task management
* Operazione di mantenimento

CERCARE DI UTILIZZARE LA VERSIONE 23, LA 24 è BUGGATA

Un'alternativa è **MySQL workbench**, molto più professionale di DBeaver

All'esame si utilizza DBeaver

## Accesso al db tramite python
Lo facciamo tramite una libreria, `mysql-connector-python`, ossia una serie di metodi e classi che ci permettono di interagire con un 
**server sql**

I diversi vendor (MariaDB, MySQL, etc...) hanno standard leggermente diversi. Esiste un sito che realizza il comparison 
sul livello di compliance agli standard SQL
Le librerie connector permettono di nascondere questi dettagli legati al singolo vendor
Tra il nostro software e il database vengono interposte delle librerie, per rendere lo standard trasparente
Noi parliamo solo con le librerie --> Che poi traducono tutto

Python definisce una serie di standard, tra cui il PEP-249 che definisce gli standard per l'interfacciamento con i DBMS
Determina quali contenuti deve avere una libreria per connettersi ad un database. 
Tutte le librerie devono fornire 2 strumenti: 
* Connection
* Cursor
Sono comodi per abilitare il cambio di libreria (e quindi di DBMS) senza dover ri-scrivere tutto

Posso installare la libreria esattamente come con flet (pip) oppure nel virutal-environment (pycharm)
Meglio se viene aggiunto nel file requirements.txt
```
flet~=0.19.0
networkx~=3.2.1
mysql-connector-python~=8.3.0
```

## Oggetto Connection
E' una funzione che ci permette di stabilire una connessione con il database server, attraverso il metodo 
`connect`. 
I parametri passati alla connect sono le credenziali di accesso al database e l'host su cui si trova. 
Tutti i database sono protetti  
Nel nostro caso sarà sempre un database locale, non su server remoto  
E' necessario anche specificare il nome del database a cui connettersi (su un host posso avere più database) tramite il **nome**
La password viene specificata quando si installa il server (spesso con valori di default)
Viene creato un oggetto di tipo `MySQLConnection` che poi permette di gestire la connessione. 

Nota: tutte le connessioni devono anche essere chiuse perchè utilizzano delle risorse computazionali del computer fino a quando non vengono chiuse.
```python
cnx.close()
```
Dopo averla utilizzata
Il programma può utilizzare anche più connessioni in parallelo, tramite il **ConnectionPooling**
### Eccezioni durante l'apertura
Bisogna gestire le eccezioni di apertura:
* Credenziali errate `ERR_ACCESS_DENIED_ERROR` --> Password e/o nome utente errati
* Database non esistente `ER_BAD_DB_ERROR`
* Il Server è spento --> Controllare se il server locale è in esecuzione. Tipicamente si trova tra i servizi

### Struttura comoda
```python
try:
    cnx = mysql.connector.connect(...)
except error:
    # gestione errori
else:
    cnx.close()
```

Nel ramo else mettere sempre la chiusura della connessione quando il codice termina

### Option file
Meglio passare le informazioni private tramite un option file, specificandolo come parametro
```python
cnx = connection(option_files="/etc/mysql/connectors.cnf")
```
Ognuno deve avere il suo file di specifiche mentre il codice può rimanere lo stesso. 
E' importante modificare il file con le credenziali giuste
