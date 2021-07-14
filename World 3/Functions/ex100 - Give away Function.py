from time import sleep
from random import sample
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def raflle(list):
    print("The numbers are:", end=" ")
    for c in list:
        print(f"{colors['blue']}{c}{colors['clean']}", end=" ")
        sleep(0.5)
    print()


def even(list):
    sumtotal = 0
    for value in list:
        if value % 2 == 0:
            sumtotal += value
    if sumtotal != 0:
        print(f"{colors['green']}The even sum is {sumtotal}{colors['clean']}")
    else:
        print(f"{colors['red']}You do not have even numbers{colors['clean']}")


numbers = sample(range(999), 5)
raflle(numbers)
even(numbers)
