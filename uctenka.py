# uctenka.py
#Autor: Jan Hruza

# Trida reprezentujici polozku na uctence
class Polozka:
    def __init__(self, nazev: str, cena: float, mnozstvi: int = 1):
        self.nazev = nazev
        self.cena = cena
        self.mnozstvi = mnozstvi
        self.celkem = cena * mnozstvi

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
    print("\n----- UCTENKA -----")
    celkova_cena = 0.0
    for polozka in polozky:
        print(f"{polozka.nazev} x{polozka.mnozstvi} @ {polozka.cena:.2f} Kc = {polozka.celkem:.2f} Kc")
        celkova_cena += polozka.celkem
    print("-------------------")
    print(f"Celkova cena: {celkova_cena:.2f} Kc")

# Hlavni funkce
def main():
    polozky = []
    while True:
        polozka = nacti_polozku()
        if polozka.nazev == "":
            break
        polozky.append(polozka)

    vytiskni_uctenku(polozky)
    
# Spusteni hlavni funkce
if __name__ == "__main__":
    main()