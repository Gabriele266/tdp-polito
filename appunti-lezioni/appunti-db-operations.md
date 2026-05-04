
# Operazioni sul DB MariaDB
Il server viene gestito dal processo `mariadbd`. Viene eseguito in automatico all'avvio. 
Se non è presente tra i processi attivi, significa che è andato in errore. 

Prima di svolgere operazioni distruttive (eventualmente anche in modalità recovery) è utile 
eseguire un **dump** del database e un **backup**. 

## Backup del database

### Dump database
Crea uno script SQL con istruzioni CREATE DATABASE, CREATE TABLE, etc... che permetta di ricostruire l'intera struttura del database
(o di tutti i database presenti sulla macchina). 

`mysqldump -u root -ppassword --all-databases > backup_completo.sql`
Per eseguire il comando è necessario identificarsi come utente --> "root" è il nome utente.
Dopo la -p è necessario inserire la password dell'utente
Questo comando crea il dump di tutti i database `--all-databases` in un file `backup_completo.sql`  
  
E' successivamente possibile ri-eseguire le istruzioni SQL nel dump per creare di nuovo il db
`mysql -u root -p nome_database < backup.sql`

Di default il dump contiene sia la struttura che i dati

### Backup fisico
In mariadb i dati sono salvati nella cartella `/opt/homebrew/var/mysql/`. 
Per effettuare un backup fisico basta **copiare l'intero contenuto della cartella da un'altra parte**

## Operazioni sugli utenti
Accedendo tramite il comando `mariadb` è possibile effettuare il login come root. 
Per creare un nuovo utente:
`CREATE USER 'user'@'localhost' IDENTIFIED BY '<password>'`

Successivamente è necessario fornire le autorizzazioni al nuovo utente per operare sui database
Autorizzazione per tutte le operazioni su un singolo database:  
```sql
GRANT ALL PRIVILEGES ON mio_database.* TO 'mario'@'localhost';
```
Che è ottimale in termini di sicurezza

Dopo aver impostato dei privilegi è necessario salvarli tramite **flush**:
```sql
FLUSH PRIVILEGES;
```
  
Per visualizzare tutti gli utenti presenti sulla macchina basta guardare il contenuto della tabella `mysql.user`:
```sql
SELECT User, Host FROM mysql.user;
```  

Per connettermi al database con uno specifico utente su un certo database:
`mysql -u nome_utente -p nome_database` Mi richiederà la password

E' buona pratica, dopo aver creato un utente, testarlo (verificando di poter fare le azioni che servono) connettendosi e provando dei comandi.