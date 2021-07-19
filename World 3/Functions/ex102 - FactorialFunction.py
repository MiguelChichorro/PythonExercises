from time import sleep
from utilities import database
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def factorial(a=0, b="", show=False):
    """
    :param a: Receive the number in n
    :param b: Receive the value in ans2
    :param show: show the account solution
    :return: return the account result
    """
    fat = 1
    if b == 'Y':
        show = True
    for c in range(a, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(f" x ", end=" ")
            else:
                print(f" = ", end=" ")
            sleep(0.5)
        fat *= c
    print(fat)


ans = 1
while ans == 1:
    n = int(input("Enter the number you want to do a factorial: "))
    ans2 = str(input(f"Do you want to see the calule? [{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]
    database.Choice(ans2)
    factorial(n, ans2)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
