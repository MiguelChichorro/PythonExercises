from time import sleep

colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


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
    print(f"{colors['purple']}Reading data...{colors['clean']}")
    sleep(1)
    print(f"{colors['yellow']}The number is {value}{colors['clean']}")


ans = 1
while ans == 1:
    lenIn("Enter a number:")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
