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
    valueseven = list()
    valuesodd = list()
    conteven = contodd = 0
    while True:
        print(f"{colors['yellow']}If you want to stop just enter 0{colors['clean']}")
        n = int(input("Enter a number: "))
        if n not in values:
            values.append(n)
            if n != 0:
                print(f"{colors['green']}Value added{colors['clean']}")
            if n % 2 == 0 and n != 0:
                valueseven.append(n)
                conteven += 1
            if n % 3 == 0 and n != 0:
                valuesodd.append(n)
                contodd += 1
        else:
            print(f"{colors['red']}Duplicate value don´t added{colors['clean']}")
        if 0 in values:
            values.remove(0)
            values.sort()
            valuesodd.sort()
            valueseven.sort()
            break
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print(f"{colors['yellow']}Your complete list is {values}{colors['clean']}")
    if conteven == 0:
        print(f"{colors['red']}You don´t enter any even number{colors['clean']}")
    else:
        print(f"{colors['purple']}Your even list {'Just have one number' if conteven == 1 else 'is'} {valueseven}{colors['clean']}")
    if contodd == 0:
        print(f"{colors['red']}You don´t enter any odd number{colors['clean']}")
    else:
        print(
            f"{colors['purple']}Your odd list {'Just have one number' if contodd == 1 else 'is'} {valuesodd}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")