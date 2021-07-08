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
    guys = list()
    data = list()
    bigweight = smallweight = 0
    ans2 = 'Y'
    while ans2 == 'Y':
        data.append(str(input("Name: ")))
        n = int(input("Weight: "))
        if n >= 100:
            bigweight += 1
        else:
            smallweight += 1
        data.append(n)
        guys.append(data[:])
        data.clear()
        ans2 = str(input("Want continue? [Y/N]")).upper()
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print(f"{colors['yellow']}You enter {len(guys)} {'just one person' if len(guys) == 1 else 'people'}{colors['clean']}")
    if bigweight == 0:
        print(f"{colors['green']}You don´t enter people with big weight{colors['clean']}")
    else:
        print(f"{colors['green']}{'just one person' if bigweight == 1 else 'These people'} has a big weight {colors['clean']}")
        for c in guys:
            if c[1] >= 100:
                print(f"{colors['yellow']}{c[0]}{colors['clean']}", end=" ")
    if smallweight == 0:
        print(f"{colors['green']}You don´t enter people with big weight{colors['clean']}")
    else:
        print(f"\n{colors['green']}{'just one person' if smallweight == 1 else 'These people'} has a small weight{colors['clean']}")
        for c in guys:
            if c[1] <= 70:
                print(f"{colors['yellow']}{c[0]}{colors['clean']}", end=" ")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
