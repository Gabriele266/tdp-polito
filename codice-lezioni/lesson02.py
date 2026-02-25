from enum import Enum

class Prodotto:
    aliquota_iva = 0.20

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def price(self):    # questo è il getter
        return self._price

    @price.setter
    def price(self, value: float):      # setter
        if value > 0:
            self._price = value
        else:
            raise ValueError("Attenzione, il prezzo non può essere negativo")

class CustomerCategory(Enum):
    GOLD = 1,
    SILVER = 2,
    BRONZE = 3,

    def stringify(self):
        if self.GOLD:
            return "Gold"
        elif self.SILVER:
            return "Silver"
        else:
            return "Bronze"

class Cliente:
    def __init__(self, name: str, email: str, category: str):
        self.name = name
        self.email = email
        self.category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        if value != "Gold" or value != "Silver" or value != "Bronze":
            raise ValueError("Attenzione, il valore passato non va bene")

        self._category = value

print(Prodotto.aliquota_iva)
print("Ora lo cambio")
Prodotto.aliquota_iva = 0.35
print(Prodotto.aliquota_iva)

p = Prodotto("Ciao", 20)
print(p.aliquota_iva)

c = Cliente("Gabriele", "Ciao", "Gold")