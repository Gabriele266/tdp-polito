# Moduli in Python

Sono una collezione di classi, funzioni, variabili e dichiarazioni

`import` esegue il sorgente del modulo e rende disponibili le definizioni
Tutte le definizioni sono create in un **namespace** diverso

https://pypi.org/ comodo per scaricare a mano dei moduli

Ogni modulo è un file python, il nome del namespace è il nome del file Python
Tutto ciò che è top-level diventa accessibile dall'esterno

Ci sono due modi di fare import:
* `import module_name` --> Dovrò sempre mettere `module_name.<qualcosa>`
* Posso cambiare il nome ad un modulo usando la keyword `as other_name`
* Utilizzando la `from` importo una dichiarazione precisa nel mio namespace
* `from module_name import *` importa tutto e rende disponibile

I moduli non dovrebbero eseguire codice quando vengono importati

Le cartelle vengono chiamate **packages**. Ogni package può avere del codice da eseguire come inizializzazione, nel file
`__init__.py`. Viene eseguito quando un qualunque modulo è importato

Posso creare un ambiente virtuale che contiene tutte le dipendenze (con le specifiche versioni) per il mio progetto,
il **virtual environment**. E' una copia locale dell'interprete
nella cartella `.venv`

Nel file `requirements.txt` esprimo tutte le dipendenze del progetto

https://file.didattica.polito.it/dl/MATDID/34063457

## Unit testing
Per scrivere unit tests si utilizza la libreria builtin `unittest`.
Il codice dei test viene raccolto in un file, all'interno di una classe che estende la classe di base `unittest.TestCase`

```python
import unittest # importo il modulo

class TestCase(unittest.TestCase):
    def test_<qualcosa>(self):
        pass
```

Ogni test è una funzione che **deve iniziare con** `test_`, altrimenti non vengono trovati
Per eseguire i test, bisogna eseguire il modulo che contiene i test come **programma principale**. Per evitare che i test non vengono trovati, è 
utile separare la logica dal main
E' normale che eseguendo dalla freccia verde della classe i test non vengano trovati.
E' utile aggiungere il blocco: 

```python
if __name__ == '__main__':
    unittest.main()
```
Per far eseguire i test quando si esegue il modulo come principale