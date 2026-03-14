# dizionari
from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    name: str
    price: float

    def __hash__(self):
        return hash((self.name, self.price))

    def __str__(self):
        return f"Prodotto {self.name} al prezzo di {self.price}"
#
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200),
    "LAP002": ProdottoRecord("Laptop Pro", 2300),
    "LAP003": ProdottoRecord("Mouse", 60),
}

print(catalogo["LAP001"])

print(catalogo.get("MIANONNA"))     # utile per effettuare controlli e più performante
r = catalogo.get("CIAO", ProdottoRecord("None", 0))     # se la chiave CIAO non esiste restituisce un prodotto vuoto
print(r)

keys = catalogo.keys()
values = catalogo.values()
items = catalogo.items()        # coppie ordinate (chiave-valore) come vettore di tuple

print(keys)
print(values)
print(items)

prezzi = {codice: prod.price for codice, prod in catalogo.items()}
print(prezzi)