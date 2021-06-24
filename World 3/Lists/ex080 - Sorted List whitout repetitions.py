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
    cont = 0
    while True:
        cont += 1
        print(f"{colors['yellow']}if you want to stop just enter 0{colors['clean']}")
        n = int(input("Enter a number:"))
        if n not in values:
            if cont == 1 or n > values[-1]:
                values.append(n)
                print(f"{colors['green']}Value added on the final position{colors['clean']}")
            else:
                pos = 0
                while pos < len(values):
                    if n <= values[pos]:
                        values.insert(pos, n)
                        break
                    pos += 1
                if n != 0:
                    print(f"{colors['green']}Value added on the position {pos}{colors['clean']}")
        else:
            print(f"{colors['red']}Duplicate value don´t added{colors['clean']}")
        if 0 in values:
            values.remove(0)
            break
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print(f"the values enter in order were {values}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
