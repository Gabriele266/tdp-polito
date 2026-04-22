
# Ricorsione
Una funzione è ricorsiva quando all'interno della funzione stessa viene richiamata se stessa

Può farlo in modo diretto o indiretto

In generale, il termine indefinito viene richiamato anche nella definizione

`mid = len(houses) // 2` L'operatore `//` effettua la divisione con floor (arrotonda)
Se la ricorsione non ha una condizione di termine, in teoria viene eseguita all'infinito. In python 
esiste il `RecursionError`, lanciato quando la ricorsione continua a non terminare. 

La ricorsione è utile nei problemi divide-et-impera: macro-problema difficile da risolvere, che può essere scomposto in sotto-problemi
più semplici, andando a risolvere solo il problema più semplice di tutti. 

Anche l'esplorazione o enumerazione è comoda da risolvere in modo iterativo. Ad esempio esplorare un grafo o trovare il percorso
di minimo costo. 

Inoltre è utile anche per le strutture dati ricorsive. 

Pseudo-codice per il divide-et-impera:
```
def solve(problem):
    if is_trivial(problem):     # controllo se è un problema talmente semplice da saperlo risolvere subito. E' la condizione di uscita
        solution = resolve_trivial(problem)     # calcolo la soluzione non utilizzando la ricorsione
        return solution
    else:
        # divido il problema in sotto problemi
        sub_problems = divide(problem)
        # raccolgo le soluzioni per tutti i problemi separati
        sub_solutions = []
        for sub_prob in sub_problems:
            sub_solutions.append(solve(sub_prob))       # uso la ricorsione per risolvere questo problema più piccolo
            
        solution = combine(sub_solutions)               # combino le soluzioni dei sotto-problemi in un unica soluzione
        return solution     
```

## Struttura esplorativa
Ho una serie di step. C'è sempre una condizione terminale
Ogni volta, eseguo uno step, esploro e poi annullo lo step

## Efficienza della ricorsione
Utilizzando la ricorsione, posso trovarmi nel caso in cui alcuni elementi foo(X) vengono computati più volte, 
soprattutto nella struttura divide-et-impera (più macro-problemi che danno luogo a parti della stessa suddivisione)

Non partire subito dalla soluzione migliore, prima qualcosa di meno ottimizzato
Una tecnica per migliorare l'efficienza è quella di utilizzare una cache in cui memorizzare un elemento che è già stato computato
Ho 2 approcci:
* Implementarla io tramite un dizionario --> la chiave è il valore del parametro, il valore è l'ultimo computato
* Utilizzare il decoratore `@lru-cache` sulla funzione ricorsiva --> Fa tutto lui