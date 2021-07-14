colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
numbers = list()


def big(list):
    cont = bigger = smaller = 0
    while cont < len(list):
        if cont == 0:
            bigger = list[cont]
            smaller = list[cont]
            cont += 1
        else:
            if list[cont] >= bigger:
                bigger = list[cont]
                cont += 1
            elif list[cont] <= smaller:
                smaller = list[cont]
                cont += 1
    print(f"{colors['purple']}Your list is {numbers} and the bigger value is {bigger} and the smaller value is {smaller}{colors['clean']}")


while True:
    print("Enter zero to stop.")
    n = int(input("Enter a number:"))
    if n == 0:
        break
    else:
        numbers.append(n)
        numbers.sort()
big(numbers)
