from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def helpi(n):
    print(colors['green'], end="")
    print(help(n))
    print(colors['clean'], end="")


def title(msg, color=""):
    tam = len(msg) + 3
    print(colors[color], end="")
    print("=" * tam)
    print(f"    {msg}")
    print("=" * tam)
    print(colors['clean'], end="")


while True:
    title("Pyhelp", "yellow")
    print(f"{colors['red']}Enter 'end' To finisinh the program{colors['clean']}")
    lin = str(input(f"{colors['cian']}Enter some python command: {colors['clean']}")).lower()
    print(f"{colors['purple']}Reading data...{colors['clean']}")
    sleep(1)
    if lin != "end":
        helpi(lin)
    else:
        break
title("Have good day", "green")
