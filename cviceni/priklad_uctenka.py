# uctenka.py
#Autor: Jan Hruza

from polozka import Polozka
from uctenka import Uctenka

# Funkce pro nacteni polozky od uzivatele
def nacti_polozku() -> Polozka:
    nazev = input("Zadejte nazev polozky (nebo prazdny retezec pro konec): ")
    if nazev == "":
        return Polozka("", 0.0, 0)
    
    cena = float(input("Zadejte cenu polozky: "))
    mnozstvi = int(input("Zadejte mnozstvi polozky: "))
    return Polozka(nazev, cena, mnozstvi)

# Funkce pro vytisknuti uctenky
def vytiskni_uctenku(polozky: list[Polozka]) -> None:
    # print("----- UCTENKA -----")
    # celkova_cena = 0.0
    # for polozka in polozky:
    #     print(polozka)
    #     celkova_cena += polozka.celkem
    # print("-------------------")
    # print(f"Celkova cena: {celkova_cena:.2f} Kc")

    uctenka = Uctenka()
    for polozka in polozky:
        uctenka.PridatPolozku(polozka)

    print(uctenka)

# Hlavni funkce
def main():
    polozky = []
    while True:
        polozka = nacti_polozku()
        if polozka.nazev == "":
            break
        polozky.append(polozka)
    
    print()
    vytiskni_uctenku(polozky)
    
# Spusteni hlavni funkce
if __name__ == "__main__":
    main()