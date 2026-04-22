import time
from functools import lru_cache

import matplotlib.pyplot as plt

class Fibonacci:
    def __init__(self) -> None:
        self.cache: dict[int, int] = {          # inizializzo la cache con i valori noti dell'algoritmo
            0: 0,
            1: 1,
        }
        self.calls_n = 0
        self.calls_n_cache = 0

    def fibonacci_base(self, n: int) -> int:
        self.calls_n += 1
        if n == 0 or n == 1:
            return n

        else:
            return self.fibonacci_base(n - 1) + self.fibonacci_base(n - 2)

    @lru_cache(maxsize=None)
    def fibonacci_lru(self, n: int) -> int:
        self.calls_n_cache += 1
        if n == 0 or n == 1:
            return n

        else:
            return self.fibonacci_base(n - 1) + self.fibonacci_base(n - 2)

    def fibonacci_cached(self, n: int) -> int:
        self.calls_n_cache += 1
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = self.fibonacci_cached(n - 1) + self.fibonacci_cached(n - 2)     # l'ottimizzazione ha senso perchè ogni volta la chiamata si spezza in 2, avviando 2 nuovi rami di ricorsione

        return self.cache[n]

    def clear_cache(self) -> None:
        self.cache = {
            0: 0,
            1: 1
        }
        self.calls_n = 0
        self.calls_n_cache = 0

def linspace(start, stop):
    l = []
    while start < stop:
        l.append(start)
        start += 1
    return l

def main():
    K = 30          # maximum value to compute
    # creating a plot to confront normal-optimized difference in time
    fibonacci = Fibonacci()
    normal_times = []
    optimized_times = []
    normal_calls = []
    optimized_calls = []

    for k in range(K):
        tick = time.time()
        r1 = fibonacci.fibonacci_base(k)
        tock = time.time()
        t1 = tock - tick
        normal_times.append(t1)
        normal_calls.append(fibonacci.calls_n)

        print(f"Computed element with normal recursion {k}: {tock - tick} ms, --> {r1} result ")

        tick = time.time()
        r2 = fibonacci.fibonacci_cached(k)
        tock = time.time()
        t2 = tock - tick
        optimized_times.append(t2)
        optimized_calls.append(fibonacci.calls_n_cache)

        print(f"Computed element with optimized recursion {k}: {tock - tick} ms, --> {r2} ")

        #time_ratio = t2 / t1
        #print("Time ratio (t2/t1) %: ", time_ratio * 100)

        if r1 == r2:
            print("Everything OK")

        fibonacci.clear_cache()     # otherwise cache would impact a lot more

    plt.figure()
    plt.subplot(211)
    plt.plot(linspace(0, K), normal_times, label="Normal recursion")
    plt.ylabel("Time (ms)")
    plt.title("Comparison of normal and optimized recursions for fibonacci")
    plt.plot(linspace(0, K), optimized_times, label="Optimized recursion")
    plt.legend()
    plt.subplot(212)
    plt.plot(linspace(0, K), normal_calls, label="Normal recursion")
    plt.plot(linspace(0, K), optimized_calls, label="Optimized recursion")
    plt.ylabel("Number of calls [n]")
    plt.xlabel("Number of elements [n]")
    plt.show()
if __name__ == "__main__":
    main()