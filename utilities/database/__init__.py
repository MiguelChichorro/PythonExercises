from time import sleep

import requests
from requests import get
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def Reading():
    print(f"{colors['purple']}Reading data...{colors['clean']}")
    sleep(1)


def lenCoin(msg):
    val = False
    while not val:
        enter = str(input(msg)).replace(",", ".").strip()
        if enter.isalpha() or enter == "":
            print(f"{colors['red']}Error \"{enter}\" Impossible value{colors['clean']}")
        else:
            val = True
            return float(enter)


def lenIn(msg):
    while True:
        try:
            n = int(input("Enter a int number: "))
        except (ValueError, TypeError):
            print(f"{colors['red']}Error try to put a int number{colors['clean']}")
            continue
        except (KeyboardInterrupt):
            print(f"\n{colors['red']}Data Enter interrupt{colors['clean']}")
            return 0
        else:
            return n


def lenFloat(msg):
    while True:
        try:
            n = float(input("Enter a float number: "))
        except (ValueError, TypeError):
            print(f"{colors['red']}Error try to put a float number{colors['clean']}")
            continue
        except (KeyboardInterrupt):
            print(f"\n{colors['red']}Data Enter interrupt{colors['clean']}")
            return 0
        else:
            return n


def Choice(ans2=""):
    while ans2 != "Y" and ans2 != "N":
        ans2 = str(input(f"{colors['red']}Please just enter Yes or No {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]


def pudim():
    try:
        response = requests.get('https://sell.sawbrokers.com/domain/pudim.com/')
    except:
        print(f"{colors['red']}I can´t connected with Pudim ;----;{colors['clean']}")
    else:
        print(f"{colors['green']}I connected with Pudim :D{colors['clean']}")