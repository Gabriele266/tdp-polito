# Algoritmi utili sui grafi

## Note utili
* Evitare di mettere if con return anticipate ma seguire sempre una struttura lineare if-else --> Rende più semplice il backtracking
* Aggiungere subito il nodo corrente al percorso di nodi visitati --> Così non ci sono problemi nel conteggio dei nodi
* Mettere il backtracking sempre alla fine della funzione, MANTENENDO UN UNICO PUNTO DI USCITA (append --> codice funzione --> pop)
* Per il backtracking, utilizzare la `pop` e NON la `remove` che è più costosa
* Il backtracking deve sempre **ripristinare lo stato della memoria condivisa** alla **situazione in cui era prima della chiamata** alla funzione
  - Ciò che aggiungo va tolto
* La soluzione finale **deve essere sempre copiata** (`mialista.copy()`) per evitare che qualcuno la modifichi
* La ricorsione può essere anche utilizzata per **"pescare" nodi dalle diverse componenti connesse**, associando ad ogni componente connessa un indice
* Verificare sempre le condizioni di potatura, cercando anche di **prevedere se il branch che si sta per creare può portare ad una soluzione o meno**
* I **cammini devono essere semplici** --> Verificare di **non ri-visitare lo stesso nodo più volte** (`if next not in visited`). Se aggiungo subito il nodo a visited, il controllo deve essere fatto sul nuovo nodo successivo (E NON SUL NODO CORRENTE)
* Attenzione ai **nomi utilizzati nelle variabili locali della funzione ricorsiva**, **non** devono **sovrascrivere** parametri della funzione

## DFS Con numero esatto di archi nel percorso
Ricerca di un percorso da `start` fino a `end` con esattamente il numero di archi `max_len` e funzione obiettivo massimizzata, su grafo direzionato e pesato.

```python
def get_path(self, start: Product, end: Product, max_len: int)-> list[Product] | None:
    self.__best_target_function = -1
    path = []
    self.best_path = None
    self.__explore_node_dfs(start, path, max_len, 0, end)

    return self.best_path


def __explore_node_dfs(self, node, visited, max_len, partial_weight_sum, path_end: Product):
    graph = self.graph
    visited.append(node)        # Aggiungo subito il nodo

    # Condizioni di potatura
    if node == path_end and len(visited) == max_len:        # Condizione di raggiungimento della destinazione
        # Percorso fino alla destinazione con esattamente il numero di archi max_len
        if partial_weight_sum > self.__best_target_function:
            self.__best_target_function = partial_weight_sum
            self.best_path = visited.copy()
            # Verifico se il percorso è maggiorativo rispetto al migliore che ho già trovato
    elif len(visited) < max_len and node != path_end:       # Espansione dell'albero
        # Esploro i nuovi nodi che posso raggiungere
        edges = graph.out_edges(node, data=True)
        for _, destination, data in edges:  # E' più comodo utilizzare la notazione explode sulla tripla
            weight = data["weight"]
            if destination not in visited:  # Esploro un nuovo nodo solo se non lo ho ancora visitato
                self.__explore_node_dfs(destination, visited, max_len, partial_weight_sum + weight, path_end)

    visited.pop()       # Backtracking, UNICO PUNTO DI USCITA
```

Qui la spiegazione del backtracking e della logica
[Backtracking ricerca cammino massimo.pdf](Backtracking%20ricerca%20cammino%20massimo.pdf)

## Valutazione dell'intersezione a coppie
Utile per valutare se due entità hanno un'itersezione (ad esempio dei film in comune) a partire da una tabella che fornisce le statistiche utili. 

```python
statistic_table = DAO.get_statistics_table(min_rating, max_rating)

for a, b in itertools.combinations(actors, 2):
    # Film in cui ha recitato l'attore A, sotto forma di id-map a partire dalla tabella statistiche
    films_a = self.load_films_for_actor(a.id, statistic_table)

    # Film in cui ha recitato l'attore B
    films_b = self.load_films_for_actor(b.id, statistic_table)

    intersection = set(films_a.keys()) & set(films_b.keys())
    if len(intersection) > 0:    # I due attori hanno almeno un film in comune
        movies_in_common = { k: films_a[k] for k in intersection}       # Informazioni sui film in comune prese dalla tabella delle statistiche
        weight = self.__calc_weight(movies_in_common)
        self.graph.add_edge(a, b, weight=weight)

def load_films_for_actor(id: str, all_actors_stat):
    id_map = defaultdict()

    for a_row in all_actors_stat:
        if a_row["actor_id"] == id:
            id_map[a_row["movie_id"]] = a_row["worlwide_gross_income"]

    return id_map
```

## Ricerca dei migliori nodi con funzione obiettivo
Per **ricercare i migliori nodi** che possiedono una certa **caratteristica numerica** (ad esempio i nodi con valore più alto di un certo campo), 
è utile fare una funzione per **calcolare su ogni nodo il valore obiettivo**. 
La struttura dati per raccogliere questa informazione è una **LISTA IN CUI LE RIGHE SONO DIZIONARI CON COPPIE IDNODO-VALORE**
L'**ordinamento della lista viene fatto sul valore**, per poi associare le informazioni complete dell'oggetto grazie alla rispettiva ID map
NON UTILIZZARE DIRETTAMENTE UNA ID-MAP PERCHè NON PERMETTE DI ORDINARE

Esempio di codice: 
```python
def get_best_5_products(self):
    stats = []      # La struttura dati è una lista di dizionari
    # [{'id': 48, 'value': 1746}, {'id': 56, 'value': 1746}, {'id': 52, 'value': 1380} ]

    for product in self.graph.nodes:
        uscenti = self.graph.out_edges(product, data=True)
        entranti = self.graph.in_edges(product, data=True)

        peso_uscenti = sum([u[2]["weight"] for u in uscenti])       # Per calcolare la somma dei pesi degli archi è comodo mappare in una nuova lista (notazione [... for ...]) e poi passarla alla funzione sum
        peso_entranti = sum([e[2]["weight"] for e in entranti])
        
        stats.append({"id": product.id, "value": peso_uscenti - peso_entranti})     # Aggiungo alla struttura dati

    return sorted(stats, key=lambda row: row["value"], reverse=True)[0:5]           # Ordino la lista sulla base dei valori della chiave "value" di ogni riga e restituisco i primi 5
```

## Pescaggio di un set di K elementi da K componenti connesse diverse con funzione obiettivo
L'algoritmo prevede di pescare un **set ottimo di K elementi** prendendone al massimo **1 per ogni componente connessa** in modo ricorsivo,
verificando l'**ottimalità** della soluzione tramite un certo **criterio**. 
Ad ogni componente connessa si associa un indice, ogni volta si spawnano 2 branch: uno in cui si utilizza la componente connessa (che si sotto-ramifica in tutti gli elementi della componente) e uno in cui non la si usa (skippando all'indice successivo). 
La soluzione usa il backtracking per ridurre la complessità di spazio e applica condizioni di potatura per prevedere se un branch può portare ad una soluzione ammissibile o meno. 

```python
  def search_best_set(self, K: int) -> list[Pilot] | None:
        # Impossibilità del problema
      if K <= 0:
          return None

      conn_comps = sorted(nx.connected_components(self.graph), key=len)
      num_comps = len(conn_comps)
        
        # Impossibilità del problema
      if K > num_comps:
          return None

      self.best_set = None
      self.min_diff_dob = None
      visited = []

      self.__pescaggio_comp(0, num_comps, visited, K, conn_comps)
      return self.best_set

  def __pescaggio_comp(self, indice_comp: int, num_conn_comps: int, visited: list[Pilot], K: int, conn_comps: list[set[Pilot]]):
      k_piccolo = len(visited)
      if k_piccolo == K:
          # Condizione di termine con verifica dell'ottimalità
          diff = ((max(visited, key=lambda p: p.dob).dob) - (min(visited, key=lambda p: p.dob).dob)).days

          if self.min_diff_dob is None or diff < self.min_diff_dob:
              self.min_diff_dob = diff
              self.best_set = visited.copy()
      elif indice_comp < num_conn_comps and k_piccolo <= abs(indice_comp  - num_conn_comps):      # Verifico subito che esplorando questo ramo, si possa arrivare ad una soluzione.
          # Se il secondo controllo fallisce significa che non ci sono abbastanza componenti connesse rimanenti per arrivare ad una soluzione ammissibile
          # Posso esplorare una nuova componente
          current_component = conn_comps[indice_comp]
          for pilot in current_component:
              visited.append(pilot)
              self.__pescaggio_comp(indice_comp + 1, num_conn_comps, visited, K, conn_comps)
              visited.pop()

          # Branch non utilizzare la componente
          self.__pescaggio_comp(indice_comp + 1, num_conn_comps, visited, K, conn_comps)
```

[algoritmo-pesca-componenti.pdf](../algoritmo-pesca-componenti.pdf)