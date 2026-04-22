import time
import matplotlib.pyplot as plt

class Fibonacci:
    def __init__(self) -> None:
        self.cache: dict[int, int] = {          # inizializzo la cache con i valori noti dell'algoritmo
            0: 0,
            1: 1,
        }

    def fibonacci_base(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        else:
            return self.fibonacci_base(n - 1) + self.fibonacci_base(n - 2)

    def fibonacci_cached(self, n: int) -> int:
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

def linspace(start, stop):
    l = []
    while start < stop:
        l.append(start)
        start += 1
    return l

def main():
    K = 40          # maximum value to compute
    # creating a plot to confront normal-optimized difference in time
    fibonacci = Fibonacci()
    normal_times = []
    optimized_times = []

    for k in range(K):
        tick = time.time()
        r1 = fibonacci.fibonacci_base(k)
        tock = time.time()
        t1 = tock - tick
        normal_times.append(t1)

        print(f"Computed element with normal recursion {k}: {tock - tick} ms, --> {r1} result ")

        tick = time.time()
        r2 = fibonacci.fibonacci_cached(K)
        tock = time.time()
        t2 = tock - tick
        optimized_times.append(t2)

        print(f"Computed element with optimized recursion {k}: {tock - tick} ms, --> {r2} ")

        #time_ratio = t2 / t1
        #print("Time ratio (t2/t1) %: ", time_ratio * 100)

        if r1 == r2:
            print("Everything OK")

        fibonacci.clear_cache()     # otherwise cache would impact a lot more

    plt.plot(linspace(0, K), normal_times, label="Normal recursion")
    plt.ylabel("Time (ms)")
    plt.xlabel("Element number")
    plt.title("Comparison of normal and optimized recursions for fibonacci")
    plt.plot(linspace(0, K), optimized_times, label="Optimized recursion")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()