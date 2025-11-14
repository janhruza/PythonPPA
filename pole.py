# print_array.py
# Autor: Jan Hruza

import random

# funkce print_array(array:list[int]) -> None
# vytiskne pole ve formatu [a, b, c, ...] s carkou na konci
def print_array(array: list[int]):
    """
    Vytiskne pole ve formatu [a, b, c, ...] s carkou na konci
    """

    print("[", end = "")
    for i in range(len(array)):
        print(array[i], end=", ")

    print("]", end = "")
    return

# funkce print_array2(array:list[int]) -> None
# vytiskne pole ve formatu [a, b, c, ...] bez carky na konci
def print_array2(array: list[int]):
    """
    Vytiskne pole ve formatu [a, b, c, ...] bez carky na konci
    """

    print("[", end="")
    for i in range(len(array)):
        print(array[i], end="")
        if i != len(array) - 1:
            print(", ", end="")
    print("]", end="")

# funkce input_array(n:int) -> list[int]
# nacte n prvku od uzivatele a vrati pole
def input_array(n: int) -> list[int]:
    """
    Nacte n prvku od uzivatele a vrati pole

    Params:
        n (int): Pocet prvku k nacteni
    """

    array = [0] * n
    print(f"Nacti {n} prvku do pole")

    for i in range(n):
        try:
            value = int(input(f"Zadejte prvek {i + 1}: "))
            array[i] = value
        except ValueError:
            print("Neplatný vstup, nastavuji prvek na 0.")
            array[i] = 0

    return array

# generate_range(n:int, first:int, step:int) -> list[int]
# vygeneruje pole n prvku, prvni prvek je first, kazdy
# napr. 5, 6, -2 -> [6, 4, 2, 0, -2]
def generate_range(n: int, first: int, step: int) -> list[int]:
    array = []
    for i in range(n):
        array.append(first + i * step) # timto zpusobem se minimalizuji chyby pri zaokrouhlovani v pripade, ze by step nebyl cely cislo
    return array

# vygeneruje pole n prvku s nahodnymi hodnotami v rozsahu min az max
# pouziti random.randint
def generate_random_array(n: int, min_value: int, max_value: int) -> list[int]:
    """
    Vygeneruje pole n prvku s nahodnymi hodnotami v rozsahu min_value az max_value

    Params:
        n (int): Pocet prvku v poli
        min_value (int): Minimalni hodnota generovaneho cisla
        max_value (int): Maximalni hodnota generovaneho cisla
    """

    array = [0] * n
    for i in range(n):
        # array.append(random.randint(min_value, max_value))
        array[i] = random.randint(min_value, max_value)
    return array

# agregacni funkce max(array:list[int]) -> int
# vrati maximalni hodnotu v poli
def array_max(array: list[int]) -> int:
    """
    Vrati maximalni hodnotu v poli

    Params:
        array (list[int]): Pole cisel
    """

    max_value = array[0]
    for value in array:
        if value > max_value:
            max_value = value
    return max_value

# Hlavni program
if __name__ == "__main__":

    # vygenerovani a tisk pole
    sample_array = generate_random_array(10, 0, 100)
    print_array2(sample_array)
    print()

    # vypocet a tisk maximalni hodnoty
    max_value = array_max(sample_array)
    print(f"Maximum: {max_value}")