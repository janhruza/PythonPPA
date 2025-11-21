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
