# uctenka.py
#Autor: Jan Hruza

# Trida reprezentujici polozku na uctence
class Polozka:

    # Inicializace polozky s nazvem, cenou a mnozstvim
    def __init__(self, nazev: str, cena: float, mnozstvi: int = 1):
        self.__nazev = nazev
        self.__cena = cena
        self.mnozstvi = mnozstvi

    @property
    def nazev(self) -> str:
        return self.__nazev
    
    @property
    def cena(self) -> float:
        return self.__cena
    
    @property
    def mnozstvi(self) -> int:
        return self.__mnozstvi

    @property
    def celkem(self) -> float:
        return self.__mnozstvi * self.__cena

    @mnozstvi.setter
    def mnozstvi(self, mnozstvi:int):
        if mnozstvi < 0:
            self.__mnozstvi = 0
        else:
            self.__mnozstvi = mnozstvi

        # alternativni zapis
        # self.__mnozstvi = max(0, mnozstvi)

    # Vraci retezec reprezentujici polozku
    def __str__(self) -> str:
        return f"{self.nazev}\t{self.cena:.2f} Kc\t{self.mnozstvi} ks\t{self.celkem:.2f} Kc"

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
    print("----- UCTENKA -----")
    celkova_cena = 0.0
    for polozka in polozky:
        print(polozka)
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
    
    print()
    vytiskni_uctenku(polozky)
    
# Spusteni hlavni funkce
if __name__ == "__main__":
    main()