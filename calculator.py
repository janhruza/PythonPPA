# Simple Calculator
# Autor: Jan Hruza, Github Copilot

# Funkce pro zadani cisla s osetrenim chyb
def input_number():
    while True:
        try:
            number = float(input("Zadej cislo: "))
            return number
        except ValueError:
            print("Neplatny vstup. Zadej platne cislo.")

# Funkce pro zadani operatoru s osetrenim chyb
def input_operator():
    while True:
        operator = input("Zadej operator (+, -, *, /) nebo '=' pro ukonceni: ")
        if operator in ["+", "-", "*", "/", "="]:
            return operator
        else:
            print("Neplatny operator. Zadej jeden z +, -, *, / nebo =.")

# Hlavni program
if __name__ == "__main__":

    # deklarace promennych
    operator= ""
    result = 0

    # hlavni smycka kalkulacky
    while operator != "=":

        # pokud neni zadany operator, zada se prvni cislo
        if operator in ["+", "-", "*", "/"]:
            num2 = input_number()

            # pricitani
            if operator == "+":
                result += num2

            # odcitani
            elif operator == "-":
                result -= num2

            # nasobeni
            elif operator == "*":
                result *= num2

            # deleni
            elif operator == "/":

                # osetreni deleni nulou
                if num2 != 0:
                    result /= num2

                # pokud je deleni nulou, vypise chybu a pokusi se znovu
                else:
                    print("Chyba: Deleni nulou.")
                    continue
        else:
            result = input_number()
        
        # zadani operatoru
        operator = input_operator()

    # vypis vysledku
    print(f"Konecny vysledek: {result}")