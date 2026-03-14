from dataclasses import dataclass
from collections import Counter

@dataclass
class ClienteRecord:
    name: str
    email: str
    category: str

    def __init__(self, name: str, email: str, category: str):
        self.name = name
        self.email = email
        self.category = category


lista_clienti = [
    ClienteRecord("Mario Rossi", "mario.rossi@ciao.it", "Gold"),
    ClienteRecord("Mario Verdi", "mario.verdi@ciao.it", "Silver"),
    ClienteRecord("Mario Gialli", "mario.gialli@ciao.it", "Gold"),
    ClienteRecord("Mario VLU", "mario.vlu@ciao.it", "Bronze"),
]

categories = [c.category for c in lista_clienti]    # lista delle categorie
print(categories)
# la lista prodotta ha delle ripetizioni, posso voler contare quante occorrenze accadono per ogni categoria
categ_counter = Counter(categories)
print(categ_counter)
print(categ_counter.most_common(1)) # primi n componenti con la numerosità più elevata
print(categ_counter.total())        # totale elementi presenti