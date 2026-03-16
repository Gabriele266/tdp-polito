
# Pile e code
Nelle pile, l'ultimo inserito è quello servito per primo. 
Nelle code, il primo arrivato è servito per prima. 

Usare una lista come add e pop funziona come se fosse una pila. 
Su una lista, se faccio pop(0) è significativamente lento, perchè la lista deve rimuovere il primo e poi spostare indietro tutti gli altri. 
La complessità è O(n) rispetto ad un'operazione che potrebbe essere 1

DEQ --> Double ended queue (fornisce metodi efficienti per aggiungere e rimuovere a destra e sinistra)

`s = collections.deque()`   Crea una nuova duoble ended queue
FIFO / LIFO
Per tutti i metodi posso specificare se farlo a sinistra o a destra:
`s.appendleft(...)`
`s.popleft()`
Tutte le operazioni hanno la stessa efficienza. 
Posso anche realizzare code con dimensione fissa:
`s = collections.deque(maxlen=N)`

Il metodo `extend` aggiunge un iterable (lista, set, ...) a sinistra della lista

## Priority Queues
Code prioritarie. Ad ogni elemento si associa una priorità. Li si aggiunge in qualunque ordine, ma quando si estrae
vengono estratti in base alla priorità -> Ad esempio gli ospedali con le priorità dei codici. 

Posso scorrere una coda fino a svuotamento utilizzando:
```python
while <coda>:
    pass
```
Il ciclo si ferma quando ho poppato l'ultimo elemento