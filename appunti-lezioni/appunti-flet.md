# Flet

Flet organizza l'interfaccia grafica in gerarchie di container in cui aggiungiamo gli elementi grafici. 
E' basata su flutter.
Il container più generale è la `Page` che contiene tutta la pagina corrente. 
Gli elementi grafici sono chiamati **controlli**. Ogni controllo è una classe del modulo flet.

Per non avere problemi di versioni è comodo utilizzare un file `requirements.txt` top level in cui mettere la versione giusta che mi serve:
```
flet~=0.22.0
```

## Modifica di elementi UI per visualizzare risultati
Per modificare gli elementi UI e visualizzare dei risultati si può utilizzare questo pattern:
* Nella view, creare un puntatore all'elemento grafico da rendere dinamico
```python
import flet as ft

@ft.control
class HomePage(View, WithBanner):
    def __init__(self, page: ft.Page) -> None:
        self.__result_input = None          # dichiaro l'attributo per potervi accedere in futuro
        self.controller = SpellcheckController(self)
        super().__init__()
        WithBanner.__init__(self, page)
    
    def init(self):
        #... altre cose ....
        self.__result_input = ft.TextField(label = "", width = 300, height = 200) # creo l'elemento al difuori della struttura
        
        self.controls = [
            #... altri controlli ...,
            self.__result_input]        # metto il controllo dinamico

    def set_result(self, value):        
        if self.__result_input is not None:
            self.__result_input.value = value
```

Poi creo un metodo `set_result` per impostare il valore del campo di input dinamicamente. 
Verrà chiamato dal controller quando l'elaborazione termina
In automatico, accedendo al campo `value` l'interfaccia viene aggiornata

Nota: nel costruttore, la prima riga deve essere quella che dichiara il campo, altrimenti le chiamate super 
possono causare problemi di dipendenza circolare e non trovare l'attributo

## Visualizzazione di un set di risultati scrollabili
Per visualizzare una lista di risultati che sia scrollabile, si utilizza il controllo `ListView`.
Nota: per funzionare, è necessario dargli un'**altezza fissa** e inserirlo in un **Column**

```python
self._page.controls.append(
 ft.Column(
            controls=[ft.ListView(
                height=300,
                auto_scroll=True,
            controls=[
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("fdas"),
                ft.Text("Ciao"),
                ft.Text("fdsa"),
                ft.Text("Ciao"),
                ft.Text("Ciao"),
                ft.Text("dfsa"),
                ft.Text("Ciao"),
                ft.Text("fdsaf"),
                ft.Text("Ciao"),
            ])],
        )
)
```

Per dare un bordo alla zona della ListView è sufficiente wrappare il controllo con un `Container` ed impostargli il bordo.

## Validazione avanzata degli input field
Gli input field possono essere utilizzati sia per inserire del testo che per visualizzare delle informazioni dinamiche (quando gli passo il parametro `read_only=True`)
Posso inoltre configurare una validazione avanzata dell'input tramite regex, utilizzando: 

```python
ft.TextField(label="Matricola",
     hint_text="Inserisci una matricola",
     input_filter=ft.InputFilter(
         allow=False,
         regex_string=r"^\d{0,6}$"
     ),
     on_change=self.controller.handle_change_matricola),
```

Tramite la classe `InputFilter` ho specificato una regex per verificare che il testo inserito sia una matricola (max 6 cifre)
Esistono inoltre alcune classi che ereditano da `InputFilter` che sono già fatte.

## Impostazione delle dimensioni della finestra
```python
page.window.width = 200        # window's width is 200 px
page.window.height = 200       # window's height is 200 px
page.window.resizable = False  # window is not resizable
```