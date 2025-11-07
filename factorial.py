# factorial.py
# Autor: Jan Hruza

def fact(n:int) -> int:
    # if n < 2:
    #     return 1
    # else:
    #     return n * fact(n - 1)

    result = 1
    while n > 1:
        result *= n
        n -= 1

    return result

if __name__ == "__main__":
    print(fact(5))