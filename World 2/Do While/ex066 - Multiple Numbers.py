colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    n = cont = sum = 0
    while True:
        n = int(input("Enter how many numbers you want (999 stop): "))
        if n == 999:
            break
        cont += 1
        sum += n
    if cont == 0:
        print(f"{colors['red']}You need to enter a number{colors['clean']}")
    elif cont == 1:
        print(f"{colors['yellow']}You just enter one number can´t do the sum{colors['clean']}")
    else:
        print(f"{colors['green']}You enter {cont} numbers and the sum between them is {sum}{colors['clean']}")
        ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
