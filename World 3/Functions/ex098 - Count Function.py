from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def count(b, e, p):
    print(f"{colors['green']}Count {b} until {e} in {p}{colors['clean']}")
    if p == 0:
        p = 1
    if b < e:
        cont = b
        while cont <= e:
            print(f"{cont}", end=" ")
            cont += p
            sleep(0.4)
        print()
    else:
        cont = b
        while cont >= e:
            print(f"{cont}", end=" ")
            cont -= p
            sleep(0.4)
        print()


count(1, 10, 1)
count(10, -1, 2)
print(f"{colors['green']}------ Personalyse Count -----{colors['clean']}")
count(b=int(input("Enter the begin: ")), e=int(input("Enter the end: ")), p=int(input("Enter the pas: ")))
