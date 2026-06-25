# Operazioni di base sui grafi
La gestione del grafo viene svolta all'interno del **model**, mettendo il `graph` come attributo privato della classe. 

Creazione di un grafo vuoto
```python
graph = nx.Graph() # Grafo non direzionato
graph = nx.DiGraph()    # Grafo direzionato
```

Per creare nodi e archi utilizzare i metodi `add_node` e `add_edge`
I nodi possono essere delle dataclass ma devono aver implementato il metodo `__hash__` ed essere hashable
E' comodo nei nodi avere un dettaglio aggiuntivo rispetto al solo id  
  
## Calcolo componenti connesse
Per ottenere il numero delle componenti connesse:
`nx.number_connected_components(graph)`

## Esplorazione dei nodi di un grafo
Per esplorare i nodi (senza seguire percorsi) e ottenere statistiche sui nodi (ad esempio il grado di ogni nodo)
è utile iterarli in questo modo: 

```python
for node, adiacents in graph.adj.items():
    neighbors = adiacents.items()
    p = len(neighbors)
```
Nelle variabili `node` e `adiacents` si trovano rispettivamente le informazioni sul nodo corrente e sui vicini raggiungibili

# Creazione di grafi con coppie di dati
Può essere utile creare grafi che considerano l'insieme dei dati a coppie per aggiungere gli archi. Per farlo è comodo utilizzare 
`itertools.combinations(all_data, N)` che crea un iteratore che fornisce tutte le tuple di dimensione N ordinate ma senza duplicati
in modo efficiente. 
  
# Grafi direzionati
Nei grafi direzionati (`DiGraph`) quando faccio una `add_edge` l'ordine dei nodi diventa il verso dell'arco. 
La **costruzione del grafo è comodo farla nel model**

Piuttosto che effettuare tante micro-query ripetute, è comodo farne una che restituisca una tabella complessiva e poi filtrare in modo diverso la tabella. 
Metodi utili: 
```python
out_edges = self.graph.out_edges(node, data=True) # Archi in uscita dal nodo che devo esplorare

# Posso scorrerli, sono delle tuple da 3 elementi (source, destination, {data})
destination = edge[1]
weight = edge[2]["weight"]
```