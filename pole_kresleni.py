# chart1 zakresli pole jako pruhovy graf
def chart1_norm(array: list[int]) -> None:
    """
    Zakresli pole jako pruhovy graf

    Params:
        array (list[int]): Pole hodnot k vykresleni
    """

    max_value = max(array)
    min_value = min(array)

    # Normalizace hodnot pro vykreslení v rozsahu 0-50
    range_span = max_value - min_value
    if range_span == 0:
        range_span = 1  # Prevence deleni nulou

    print("\nPruhovy graf:")
    for value in array:
        normalized_length = int((value - min_value) / range_span * 50)
        print(f"{value:>5} | " + "*" * normalized_length)
    print()

# chart2 zakresli pole jako sloupcovy graf
def chart2_norm(array: list[int]) -> None:
    """
    Zakresli pole jako sloupcovy graf

    Params:
        array (list[int]): Pole hodnot k vykresleni
    """

    max_value = max(array)
    min_value = min(array)

    # Normalizace hodnot pro vykreslení v rozsahu 0-20
    range_span = max_value - min_value
    if range_span == 0:
        range_span = 1  # Prevence deleni nulou

    print("\nSloupcovy graf:")
    for level in range(20, -1, -1):
        threshold = min_value + (range_span * level) / 20
        line = ""
        for value in array:
            if value >= threshold:
                line += " * "
            else:
                line += "   "
        print(f"{threshold:>5.1f} |{line}")
    print("      +" + "---" * len(array))
    print("       " + " ".join(f"{i+1:2}" for i in range(len(array))))
    print()

def generate_random_array(n: int, min_value: int, max_value: int) -> list[int]:
    """
    Vygeneruje pole n prvku s nahodnymi hodnotami v rozsahu min_value az max_value

    Params:
        n (int): Pocet prvku k vygenerovani
        min_value (int): Minimalni hodnota prvku
        max_value (int): Maximalni hodnota prvku
    """

    import random

    array = []
    for _ in range(n):
        array.append(random.randint(min_value, max_value))
    return array

# pruhovy graf bez normalizace
def chart1(array: list[int]) -> None:
    """
    Zakresli pole jako pruhovy graf bez normalizace

    Params:
        array (list[int]): Pole hodnot k vykresleni
    """

    print("\nPruhovy graf:")
    for value in array:
        print(f"{value:>5} | " + "*" * value)
    print()

# chart2 bez normalizace
def chart2(array: list[int]) -> None:
    """
    Zakresli pole jako sloupcovy graf bez normalizace

    Params:
        array (list[int]): Pole hodnot k vykresleni
    """

    max_value = max(array)

    print("\nSloupcovy graf:")
    for level in range(max_value, 0, -1):
        line = ""
        for value in array:
            if value >= level:
                line += " * "
            else:
                line += "   "
        print(f"{level:>5} |{line}")
    print("      +" + "---" * len(array))
    print("       " + " ".join(f"{i+1:2}" for i in range(len(array))))
    print()

# nacti_array(n:int) -> list[int]
# nacte od uzivatele n cisel do pole
def nacti_array(n: int) -> list[int]:
    """
    Nacte od uzivatele n cisel do pole

    Params:
        n (int): Pocet cisel k nacteni
    """

    array = []
    print(f"Nacti {n} cisel do pole:")
    for i in range(n):
        while True:
            try:
                value = int(input(f"Zadejte prvek {i + 1}: "))
                array.append(value)
                break
            except ValueError:
                print("Neplatný vstup, zadejte prosím celé číslo.")
    return array

# print_array(array:list[int]) -> None
# vypise pole na obrazovku ve formatu [a, b, c, ...]
def print_array(array: list[int]) -> None:
    """
    Vypise pole na obrazovku ve formatu [a, b, c, ...]
    """

    print("[", end="")
    for i in range(len(array)):
        print(array[i], end="")
        if i != len(array) - 1:
            print(", ", end="")
    print("]")


if __name__ == "__main__":
    # Test funkci
    pole = generate_random_array(10, 1, 10)
    print_array(pole)
    chart1(pole)
    chart2(pole)