# This is a sample Python script.
# Codice python per un semplice gestionale
# Prevedere la possibilità di definire entità che modellano i prodotti, i clienti, offrire interfaccie per calcolare i prezzi eventualmente scontati
from enum import Enum


class Prodotto:
    aliquota_iva = 0.22         # Parametro di classe, tutte le istanze avranno questo parametro

    def __init__(self, name: str, price: float, quantity: int, supplier: str) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    @classmethod
    def myclassmethod(cls, name: str):
        return cls(name, 0, 0, "foo")

    @staticmethod
    def static_qualcosa(price: float, discount_percentage: float):
        return price * (1 - discount_percentage)

    def get_product_value_gross(self) -> float:
        """A simple method to calculate the price of the product"""
        return self.get_product_value_net() * (self.aliquota_iva + 1)

    def get_product_value_net(self) -> float:
        return self.price * self.quantity

# Classe cliente, campi nome, email, categoria (gold, silver, bronze)
# Metodo descrizione che deve restituire una stringa formattata, "Cliente fulvio bianchi (Gold) - fulvio@mianonna.it"

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
    def __init__(self, name: str, email: str, category: CustomerCategory):
        self.name = name
        self.email = email
        self.category = category

    def describe_customer(self):
        return f"Cliente {self.name} {self.category.stringify()} - {self.email}"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

magazzino = [
    Prodotto("Portatile", 2000, 10, "ABC"),
    Prodotto("Mouse", price = 30, quantity = 20, supplier="CDE")
]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    val_magazzino = 0
    print(help(Prodotto.get_product_value_gross))

    for product in magazzino:
        # Tutte le proprietà sono sempre pubbliche
        print(f"Nome prodotto: {product.name}")
        print(f"Prezzo singolo: {product.price}€")
        print(f"Supplier: {product.supplier}")
        print()
        val_magazzino += product.get_product_value_gross()

    print(f'Il valore del magazzino è: {val_magazzino}€')

    aldo = Cliente("Aldo", "aldo@gmail.com", CustomerCategory.GOLD)
    print(aldo.describe_customer())