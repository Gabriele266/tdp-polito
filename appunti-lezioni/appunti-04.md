# Collections

All'interno di un dizionario, gli oggetti chiave devono essere dotati di una funzione di hash

Rendere la classe hashable 

```python
from dataclasses import dataclass

@dataclass
class MyClass:
    name: str
    prezzo_unitario: float
    
    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))
```

E' una funzione che identifica in modo univoco l'oggetto
Di solito si usano parametri della classe che siano univoci

La funzione `hash` chiama la funzione hash di una serie di oggetti (tupla) che sono i parametri univoci della classe

## Eccezione KeyError
Viene lanciata quando la chiave non esiste
E' possibile utilizzare il metodo `get` che restituisce None se l'elemento non esiste

```python
r = catalogo.get("CIAO", ProdottoRecord("None", 0))     # se la chiave CIAO non esiste restituisce un prodotto vuoto
```

E' possibile anche specificare quale valore utilizzare come default

Posso anche lavorare con un dizionario senza sapere chiavi e valori 

```python
keys = catalogo.keys()
values = catalogo.values()
```

restituiscono un oggetto set-like iterable su cui posso lavorare scorrendolo o facendo ricerche
Questi li restituiscono in modo separato. Tramite il metodo `items` posso ottenere un vettore di tuple chiave-valore

`rim = catalogo.pop("LAP003")`      rimozione di un elemento data la chiave

## Creazione nuovo dizionario tramite mappatura
` prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}` crea un nuovo dizionario a partire da quello vecchio mappando alcuni valori

Per verificare se una chiave esiste:
```python
if key in dictionary:
    ...
```

## Counter
Elaborazioni statistiche a partire da una lista

`
categ_counter = Counter(categories) 
`

Restituisce il numero di volte in cui ogni occorrenza singola avviene nella lista
Output: 
```
Counter({'Gold': 2, 'Silver': 1, 'Bronze': 1})
```