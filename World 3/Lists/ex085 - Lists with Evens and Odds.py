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
    num = [[], []]
    conteven = contodd = 0
    for c in range(0, 7):
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            num[0].append(n)
            conteven += 1
        else:
            num[1].append(n)
            contodd += 1
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    if conteven == 0:
        print(f"{colors['red']}You don´t enter any even number{colors['clean']}")
    else:
        print(f"{colors['purple']}Your even list {'Just have one number' if conteven == 1 else 'is'}\n{num[0]}{colors['clean']}")
    if contodd == 0:
        print(f"{colors['red']}\nYou don´t enter any odd number{colors['clean']}")
    else:
        print(f"{colors['purple']}\nYour odd list {'Just have one number' if contodd == 1 else 'is'}\n{num[1]}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
