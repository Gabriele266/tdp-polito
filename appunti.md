
# OOP IN Python

Una classe è uno scheletro che possiamo utilizzare (tramite il costruttore) per generare
delle entità in un programma. 

In python le proprietà sono sempre pubbliche, si possono definire ovunque nel codice
Non serve utilizzare getter/setter. 
Ci sono dei metodi per rendere le proprietà parzialmente private. 

## Costruttore
Cambia il modo in cui si definiscono i costruttori `__init__` (dunder init)
Ci sono una serie di metodi speciali per definire come un oggetto si comporta nel mondo,
i metodi **dunder**, che permettono di "educare" l'oggetto. 

Ad ogni oggetto si associa un **protocollo**, un insieme di caratteristiche minime che essi devono avere per 
essere integrati nel codice. 

## Incapsulamento
Uno dei vantaggi di utilizzare la OOP è quello di racchiudere dentro un'unica entità tutto il funzionamento
associato. Utile anche per prevenire accessi non voluti dall'esterno su valori temporanei. 
In Python ci sono delle convenzioni per rendere elementi "privati". 

## Ereditarietà
Creazione di una superclasse che poi si va a specializzare. Si basa sul principio dell'**astrazione**. 
Rappresentazioni astratte di concetti reali. 

## Polimorfismo
**typing**, se una cosa che guardo cammina come una papera e starnazza come una papera, allora è una papera. 
Lista di oggetti generici (appartenenti ad un'unica classe comune) che nascondono poi le caratteristiche specifiche
dell'istanza. 

## Overloading
Python **non ammette nativamente overloading** --> Non posso scrivere più funzioni con lo stesso nome ma argomenti diversi
perchè non è in grado di rilevare la differenza sui tipi. 

## Creazione di classi
Anche qui le classi si chiamano con la prima lettera maiuscola `Car`

In python le **proprietà si definiscono direttamente nel costruttore**

```python
class Car:
    def __init__(self, color, model, foo):
        self.color = color
        ...
```
Il costruttore è sempre **uno solo**, perchè non supporta overloading. Si utilizzano i **metodi di classe** per crearne diversi

In python le proprietà vengono associate ad un oggetto solo quando le assegno. 
Non ci possono quindi essere proprietà vuote. Il costruttore crea tutte le proprietà e le assegna 

Il parametro `self` è un riferimento all'oggetto corrente come il `this` in Java. 
Viene inserito in automatico da Python, non è necessario passarlo durante la chiamata. 
E' passato **sempre come primo argomento** ai metodi. 
Deve essere sempre utilizzato **anche quando non ci sono ambiguità**.
Per la creazione di istanze non si usa il `new`, semplicemente il nome della classe. 

`my_car = Car(...)`
Il Python è un linguaggio non tipizzato. Ogni cosa è un oggetto, anche i numeri, le stringhe, etc...

### Tipizzazione dei parametri
```python
class Prodotto:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
```
E' possibile marcare i tipi dei parametri e di ciò che restituisce un metodo. 

Inoltre posso passare i parametri tramite ordine o tramite nome:
`Prodotto("Mouse", price = 30, quantity = 20)`

## Parametri di classe
Se ho delle informazioni applicabili a tutte le istanze di una stessa classe posso utilizzare i parametri di classe

```python
class Prodotto:
    aliquota_iva = 0.20         # Parametro di classe, tutte le istanze avranno questo parametro
```
Ogni istanza della classe avrà anche questo parametro, che **potrò utilizzare allo stesso modo** ma che non viene inizializzato nel costruttore
Le variabili di istanza esistono per ogni istanza, le variabili di classe vengono create una sola volta e poi passate a tutte le istanze. 

## Metodi di classe
Posso anche creare dei metodi statici, che non appartengono alla singola istanza ma che lavorano su tutta la classe
Sono utili per il pattern singleton, per creare costruttori alternativi


```python
class MyClass:
    @classmethod
    def myclassmethod(cls, name: str):
        return cls(name, 0, 0, "foo")
```
Il `@classmethod` è un decoratore. Ogni metodo di classe riceve un riferimento alla classe stessa e non self (ossia l'istanza).
`cls` mi permette di chiamare metodi o costruttore della classe a cui appartiene.

```python
@staticmethod
def static_qualcosa(price: float, discount_percentage: float):
    return price * (1 - discount_percentage)
```

Posso anche definire dei metodi statici, che non prendono un riferimento alla classe e che svolgono 
elaborazioni separate. Per richiamare un metodo statico: `Prodotto.static_qualcosa(...)`

## Creazione di enum
Per creare una enum si utilizza la classe enum, che permette anche di creare dei metodi associati
alla enum. 

```python
from enum import Enum

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
```

## Struttura in memoria
All'inizio, l'istanza non contiene le informazioni delle proprietà fino a quando non viene chiamato il costruttore

`Car.age(mycar)` questo è un altro modo per chiamare un metodo di una classe. 

## Cose utili
`print(f'Hi, {name}')` Stringhe con interpolazione. 