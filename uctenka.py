from polozka import Polozka

class Uctenka:
    def __init__(self):
        self.__items:list[Polozka] = []

    def __str__(self):
        result = ""
        for item in self.__items:
            result += f"{item}\n"
        
        result += f"{"-" * 20}\n"
        result += f"celkem: {self.Celkem:.2f}" # opravit na cenu
        return result
    
    def PridatPolozku(self, item:Polozka):
        self.__items.append(item)

    @property
    def Celkem(self) -> float:
        total:float = 0
        for item in self.__items:
            total += item.celkem

        return total