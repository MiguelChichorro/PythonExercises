from time import sleep
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
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print(f"{colors['red']}Error write a int number{colors['clean']}")
        if ok:
            break
    Reading()
    print(f"{colors['yellow']}The number is {value}{colors['clean']}")


def Choice(ans2=""):
    while ans2 != "Y" and ans2 != "N":
        ans2 = str(input(f"{colors['red']}Please just enter Yes or No {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]