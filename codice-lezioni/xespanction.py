from typing import TypeVar, Generic

T = TypeVar("T")
def append_intelligent(destination_list: list, value: T | list[T]):
    if type(value) is list:
        for i in value:
            destination_list.append(i)
    else:
        destination_list.append(value)

def xespanction(string: str):       # str = 101X010
    l = string.find("X")

    if l == -1:         # condizione di uscita
        return string
    else:
        risultati = []
        left = string[0:l]
        right = string[l+1:]

        for c in ["0", "1"]:                # itero su tutti gli step possibili
            append_intelligent(risultati, xespanction(left + c + right))

        return risultati

if __name__ == "__main__":
    print(xespanction("010X0X0010X010X01101X0X01X"))