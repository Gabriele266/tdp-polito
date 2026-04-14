
def deliver_to(house: str):
    print(f"Deliver to {house}")


def deliver_iteratively(houses: list[str]):
    """Versione iterativa della consegna"""
    for house in houses:
        deliver_to(house)

def deliver_recursive(houses: list[str]):
    if len(houses) == 1:
        deliver_to(houses[0])
    else:
        mid = len(houses) // 2          # prendo la metà della lista
        left = houses[:mid] # prima parte della lista
        right = houses[mid:]    # seconda parte della lista
        deliver_recursive(left)
        deliver_recursive(right)

def rec_error():
    x = 10
    rec_error()

def countdown(x: int):
    if x == 0:
        print("Finish")
    else:
        l = x - 1
        print(l)
        countdown(l)

def factorial(n: int) -> int:
    if n <= 0:
        raise ValueError("Factorial is defined only for positive integers")

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomiale(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return binomiale(n - 1, k - 1) + binomiale(n - 1, k)

def is_palindrome(word: str) -> bool:
    s = len(word)
    if s == 0 or s == 1:
        return True
    else:
        l = word[0]
        r = word[s - 1]
        internal = word[1:(s - 1)]
        if l == r:
            return is_palindrome(internal)
        else:
            return False

def binomiale_factorial(n: int, k: int) -> int:
    if n < k:
        raise ValueError("Binomiale requires k to be less than n")

    return (factorial(n) // factorial(n - k)) * (1//factorial(k))

def main():
    print("Ciao")

    houses = ["A", "B", "C", "D"]
    deliver_recursive(houses)
    countdown(10)
    print(factorial(6))
    r = binomiale(6, 3)
    if r == binomiale_factorial(6, 3):
        print(f"Tutto a posto {r}")

    print(is_palindrome("kayak"))
    print(is_palindrome("paolo"))

if __name__ == "__main__":
    main()