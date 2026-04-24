# Utilizzo DBeaver
La prima cosa è connettermi ad un database o crearne uno
Poi, tramite il pannello "Diagramma" posso visualizzare il diagramma ER del database
Per eseguire uno script SQL posso utilizzare il menu "SQL Editor" e decidere se crearne uno nuovo o importarne uno
Posso modificare le tabelle tramite il pannello "Tables" dentro il db a cui sono connesso. Quando creo una nuova tabella la modifica non avviene subito. DBeaver
genera il codice SQL ma devo essere io a dirgli di applicare le modifiche tramite il pulsante "Save".  
Nel pannello data della tabella posso modificare le righe. 

## Esecuzione di uno script per la creazione del database
1. Assicurarsi di avere un solo progetto aperto in DBeaver con una sola connessione a **localhost**
2. Creare un nuovo script SQL dal menu "SQL Editor" e salvarlo con un nome sensato
3. Incollare o importare il contenuto dello script
4. Eseguirlo utilizzando il pulsante "Execute script" e non quello "Execute Query"
5. Controllare nei log di esecuzione che siano tutti "success"

Nota: Accanto al nome dello script ci deve essere il nome della connection per far sì che sia correttamente associato ed eseguibile. 
L'editor script è utile per testare le query e vedere i risultati, poi posso tradurle in query parametriche
  
Se la creazione del DB non si vede subito in DBeaver, **provare a riavviarlo.** 
