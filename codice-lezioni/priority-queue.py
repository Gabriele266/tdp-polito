
# Implementazione di coda con lista e con deque

# coda = x0 <- [x1, x2, x3, x4, x5] <- x6       coda FIFO
# con lista
import time
from collections import deque

lista = []

tic = time.time()

for x in range(100000):
    lista.append(f"x{x}")

toc = time.time()
print(toc - tic)       # Tempo impiegato
print("ms")

tic = time.time()
for i in range(100000):
    lista.pop(0)        # Li tolgo tutti

toc = time.time()           # OSS: Il tempo impiegato per la rimozione è significativamente superiore
print(f"Tempo rimozione: {toc - tic}")

d = deque()

tic = time.time()

for x in range(100000):
    d.append(f"x{x}")

toc = time.time()
print(f"Tempo aggiunta a deque: {toc - tic}")

tic = time.time()
for i in range(100000):
    d.popleft()        # Li tolgo tutti

toc = time.time()           # OSS: Il tempo impiegato per la rimozione è significativamente più ottimizzato
print(f"Tempo rimozione: {toc - tic}")