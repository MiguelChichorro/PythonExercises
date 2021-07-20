from time import sleep
from datetime import date
from utilities import database
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def line(tam=42):
    return "=" * tam


def header(txt):
    print(line())
    print(txt.center(70))
    print(line())


def menu(lista):
    header("Principal menu")
    c = 1
    for item in lista:
        print(f"{colors['yellow']}{c}{colors['blue']} - {item}{colors['clean']}")
        c += 1
    print(line())
    opc = database.lenIn(f"{colors['yellow']}Enter your option: {colors['clean']}")
    return opc
