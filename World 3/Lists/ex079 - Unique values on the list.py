from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    values = list()
    while True:
        print("if you want to stop just enter 0")
        n = int(input("Enter a number:"))
        if n not in values:
            values.append(n)
            print(f"{colors['green']}Value Added{colors['clean']}")
        else:
            print(f"{colors['red']}Duplicate value don´t added{colors['clean']}")
        if 0 in values:
            values.remove(0)
            values.sort()
            break
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print(f"{colors['yellow']}Your list is {values}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
