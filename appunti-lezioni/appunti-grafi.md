
Per fare la prova finale con TDP devo aprire una issue sull'organizzazione apposita di GitHub

# Grafi e networkx
I nodi sono dataclass che leggiamo dal database, devono essere hashable (ad esempio tramite un id)
Gli archi sono le relazioni tra le diverse tabella, rappresentate tramite delle tuple (partenza, arrivo) a cui opzionalmente posso associare
un oggetto con delle informazioni.  
Supporta anche grafi direzionati, pesati e con connessioni multiple.
Fornisce anche funzionalità per la stampa. 

C'è una serie di fermate in partenza e in arrivo, voglio poter calcolare il percorso ottimo
Il pattern id-map mappa l'id con le istanza della rispettiva classe
Il grafo deve essere creato tramite networkx, aggiungendo i nodi e gli archi. 

`add_nodes_from` permette di aggiungere una lista di nodi
`add_edge` permette di aggiungere un arco

La libreria networkx fornisce dei metodi per la ricerca del percorso minore:
* `nx.shortest_path()`
* `nx.dikjistra_path()`

Nell'esempio della metro di parigi, ci sono delle connessioni multiple (dovute alla presenza di più linee che passano lungo gli stessi nodi)
--> In questo caso si può utilizzare un multigraph, perchè altrimenti, dopo aver aggiunto tutti gli archi, osserverò che ne sono stati effettivamente messi di meno. 
Il grafo normale, se gli viene richiesto di aggiungere una connessione già presente tra due nodi, **non la aggiunge**.

Se trovo errori nel numero di nodi, può capitare che sia stata aggiunta una connessione tra due nodi che non esistono --> Vengono creati lo stesso
Il primo step è quello di **creare il grafo** a partire dal **database**. 

## Visite sul grafo
Dopo aver costruito il grafo, spesso voglio studiarne le proprietà. Tipicamente viene fissato un nodo sorgente
e poi si utilizzano due tecniche (BFS, DFS) per la visita. 

### Visita in ampiezza
Funziona per **livelli di distanza** a partire dalla sorgente
Ad ogni step mi abbasso di un livello e lo esploro, seguendo i nodi collegati

La visita produce un grafo a se stante, che viene chiamato albero di visita
--> La radice è il source
--> I nodi sono tutti i nodi che posso raggiungere da source
Sono un sotto-insieme del grafo di partenza.
Il grafo in ampiezza contiene tutti i cammini minimi che partono dal nodo source, in termini del numero di archi. 
Questo è dovuto al fatto che l'albero è costruito per livelli. 
**Questa cosa non ha più molto senso quando gli archi sono pesati**

```python
import networkx as nx

archi = nx.bfs_edges(self._grafo, source)       # restituisce un iterable di tuple rappresentante gli archi percorsi
res = []
for (partenza, arrivo) in archi:
    print(f"Arco da {partenza} a {arrivo}")
    res.append(arrivo)
```

### Visita in profondità
Parte da un nodo e va avanti fino a quando può andare, esplorando tutti i rami possibili. Una volta esplorato un ramo, si sposta ad un altro
Crea delle catene di nodi. 
E' comodo da realizzare con un algoritmo ricorsivo.

Ogni volta: guardo i nodi vicino ad s, per ognuno lo aggiungo all'albero di visita e ripeto la stessa cosa, fino a quando non ci sono più nodi vicini

I due algoritmi si utilizzano per obiettivi diversi:
DFS --> Osservazione del maggior numero di nodi nel minor tempo possibile, ad esempio per verificare se un nodo è connesso
BFS --> Ricerca del cammino minimo

Hanno tutti complessità di tempo lineare O(V + E) con V numero nodi e E numero archi
In networkx sono già implementati tramite i metodi `traversals`. 

`dfs_tree()` restituisce in output l'albero di visita

```python
albero = nx.bfs_tree(self._grafo, source)       # restituisce un albero orientato con i nodi e verfici esplorati
archi = list(albero.edges)
nodi = list(albero.nodes)

return nodi
```

L'ordine in cui compaiono i nodi nell'albero di visita è l'ordine seguito dall'algoritmo. 