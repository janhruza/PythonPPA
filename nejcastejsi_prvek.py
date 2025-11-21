# nejcastejsi_prvek.py
# Autor: Jan Hruza

import random

def nejcastejsi_prvek(pole):
        pocet_vyskytu = {}
        for prvek in pole:
            if prvek in pocet_vyskytu:
                pocet_vyskytu[prvek] += 1
            else:
                pocet_vyskytu[prvek] = 1
        
        nejcastejsi = None
        max_pocet = 0
        for prvek, pocet in pocet_vyskytu.items():
            if pocet > max_pocet:
                max_pocet = pocet
                nejcastejsi = prvek
        
        return nejcastejsi

def generuj_pole(n, rozsah):
    return [random.randint(1, rozsah) for _ in range(n)]

def main():
    pole = generuj_pole(20, 10)
    pole2 = sorted(pole)
    print("Pole:          ", end="")
    print(pole)
    print("Serazene pole: ", end="")
    print(pole2)
    vysledek = nejcastejsi_prvek(pole)
    print(f"Nejcastejsi prvek v poli je: {vysledek}")

if __name__ == "__main__":
    main()