# Algoritmi utili sui grafi

DFS Ricorsivo su grafo direzionato con backtracking per la ricerca di un ottimo, sulla base di un criterio di scelta. 

```python
def __explore_dfs(self,
                  node,     # nodo corrente da visitare
                  path,     # percorso di nodi già visitati
                 ):
    # Scorro gli archi nel caso in cui la condizione di ottimalità o di accettazione del percorso sia basata su dati degli archi
    out_edges = self.graph.out_edges(node, data=True)  # Archi in uscita dal nodo che devo esplorare

    if len(out_edges) == 0:     # La condizione di stop è quando ho raggiunto una foglia
        # Percorso terminato
        if <condizione di ottimalità>:
            # Controllo se è un nuovo ottimo
            self.max_length = len(path)  # Nuovo percorso ottimo
            self.optimal_path = [self.artist] + list(path)  # Copio il percorso per averlo da parte
    else:
        for edge in out_edges:
            destination = edge[1]
            if destination in path:         # Verifica che il percorso sia un cammino semplice
                continue

            weight = edge[2]["weight"]      # Esempio di accesso ai dati dell'arco
            if <condizione per esplorare>:
                path.append(destination)
                self.__explore_dfs(destination, path, weight)
                
                path.remove(destination)        # Backtracking
```

Qui la spiegazione del backtracking e della logica
[Backtracking ricerca cammino massimo.pdf](Backtracking%20ricerca%20cammino%20massimo.pdf)