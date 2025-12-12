import random

def generateRandomArray(n:int, min:int, max:int, seed:int | None = None) -> list[int]:
    """
    Vygeneruje nove pole podle zadanych parametru.
    
    :param n: Pocet prvku pole.
    :type n: int
    :param min: Minimalni hodnota.
    :type min: int
    :param max: Maximalni hodnota.
    :type max: int
    :param seed: Vlastni seed (voltelne).
    :type seed: int | None
    :return: Vygenerovane pole.
    :rtype: list[int]
    """

    # priprava vysledku
    result = [0] * n
    rand = random.Random(seed)

    # generovani prvku
    for i in range(len(result)):
        result[i] = rand.randint(min, max)

    # navraceni vysledku
    return result

def testIsSorted(pole:list):
    """
    Overi, zda je pole serazene a pokud ne tak vyvola AssertionError.
    
    :param pole: Pole, ktere chceme overit.
    :type pole: Seznam cisel.
    """

    # line reseni
    #assert sorted(pole) == pole, "Pole se nerovnají"

    # vyzadovane reseni
    for i in range(len(pole) - 1):
        assert pole[i] <= pole[i+1], "Neni serazeno"

def testContainsSame(data1:list[int], data2:list[int]):

    # overeni delek poli
    assert len(data1) == len(data2), "Nejsou stejne dlouha"

    # modifikovatelna kopie pole
    data3 = data1.copy()

    for i in range(len(data1)):
        assert data3.__contains__(data2[i]), "Pole nejsou stejna"
        data3.remove(data2[i])

    # nefunguje z nejakeho duvodu
    # for item in data1:
    #     found = False
    #     for i in range(len(data3)):
    #         if item == data3[i]:
    #             del data3[i]
    #             found = True
    #             break
        
    #     assert found, "Pole nejsou stejna"

def selectSort(data:list[int]):

    # delka pole
    n = len(data)

    # projde vsechny prvky
    for i in range(n):
        min_index = i

        # najde minimum v neserazene casti
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        # prohozeni prvku na aktualni pozici s nalezenym minimem v neserazene casti

        # zpusob prohozeni 1
        # data[i], data[min_index] = data[min_index], data[i]

        # zpusob prohozeni 2
        tmp = data[i]
        data[i] = data[min_index]
        data[min_index] = tmp

def main():
    """
    Hlavni metoda.
    """
    pole = generateRandomArray(10, 0, 100, None)
    pole2 = pole.copy()
    selectSort(pole2)
    testContainsSame(pole, pole2)
    print(pole)
    print(pole2)

if __name__ == "__main__":
    main()