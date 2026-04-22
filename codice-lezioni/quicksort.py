
def quicksort(arr):
    if len(arr) <= 1:
        return arr          # il vettore è composto da 1 elemento e quindi è già ordinato

    else:
        pivot = arr[0]      # Tipicamente per il quicksort scelgo il primo elemento come pivot

        more = []
        pivot_elements = []     # tutti gli elementi che sono uguali al pivot so già dove devono andare
        less = []

        for i in range(0, len(arr)):        # divido il vettore in tre vettori con tutti i numeri maggiori e minori
            if arr[i] > pivot:
                more.append(arr[i])
            elif arr[i] < pivot:
                less.append(arr[i])
            else:
                pivot_elements.append(arr[i])

        sequenza_more = [n for n in arr if n > pivot]

        return quicksort(less) + pivot_elements + quicksort(more)

if __name__ == "__main__":
    s = [2, 5, 3, 1, -20, 40]
    r = quicksort(s)
    print(r)