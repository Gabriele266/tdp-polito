from dataclasses import dataclass

# Per ciasc caso scegliere la strutt dati e scrivere il codice
# 1) Memorizzare una lista di ordiniche dovranno poi essere processatiin ordine di arrivo
# Non utilizzo una SimpleQueue --> Serve per la programmazione multithread
# Utilizzo una lista vuota a cui aggiungo e tolgo in ordine
class Ordine:
    nome: str
    price: float

ordini: list[Ordine] = []

ordini.pop() # quando li processo

# Posso anche creare una lista di tuple tempoarrivo-ordine per tenere traccia
# del momento temporale in cui è arrivato

# 2) Memorizzare i codici fiscali dei clienti
# CF_Clienti = list[str]      # una lista non va bene perchè accetta anche valori non univoci
# un SET è meglio perchè controlla che siano diversi
CF_Clienti = {"CF1", "CF2"}     # qui è meglio un SET

# 3) Database di prodotti
# Dizionario chiave-istanzaprodotto
prodotti = {
    "KEY1": Prodotto(),
}

# 4) Sede roma
# Classe che rappresenta le coordinate
@dataclass
class Coord:
    x: str
    y: str

# Oppure anche una tupla, una struttura dati immutabile

# 5) Meglio un SET
