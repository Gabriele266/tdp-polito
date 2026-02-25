# Metodi speciali

Gli **attributi di classe** sono sempre gli stessi per tutte le istanze di quella classe

Se modifico un parametro di classe dall'esterno, da quel momento in poi tutte le istanze utilizzeranno il nuovo valore

```python
class Prodotto:
    aliquota_iva = 0.22   
    
    def __init__(self):
        pass
```

Posso accedere ad un parametro di classe dall'esterno:

```python
p = Prodotto()

p.aliquota_iva = 0.30       # Modifico l'aliquota iva per tutti
Prodotto.aliquota_iva = 0.30    # Questo è più esplicito
```

## Attributi privati
Se metto un underscore prima del nome di una variabile, questa si comporta come privata. 
Utilizzando i decoratori `@property` posso creare un getter (come in Java)

```python
@property
def price(self):    # questo è il getter
    return self._price
```

Definendo questa **property** posso poi creare un setter, utilizzando il decoratore `@<property-name>.setter`

```python
@price.setter
def price(self, value: float):
    if value > 0:
        self._price = value
    else:
        raise ValueError("Attenzione, il prezzo non può essere negativo")
```
Questo setter controlla il valore della variabile e lancia un'eccezione **se il valore non va bene**

Posso anche richiamare il setter in altri punti del codice, interni alla classe --> Così incapsulo la verifica del valore

```python
self.price = price
```
Un posto utile è chiamarlo anche nel costruttore per impostare il controllo del prezzo anche sul parametro del costruttore

In Python non c'è il null ma il `None`