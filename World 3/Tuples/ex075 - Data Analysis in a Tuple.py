colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    tuple = ()
    conteven = cont3 = cont9 = 0
    for c in range(4):
        n = int(input("Enter a number between 1 and 10: "))
        if n % 2 == 0:
            conteven += 1
        tuple += n,
    if conteven == 0:
        print(f"{colors['red']}You didn´t enter any even number{colors['clean']}")
    else:
        print(f"{colors['blue']}You enter {conteven} even {'numbers' if conteven > 1 else 'number'}{colors['clean']}")
    if tuple.count(3) == 0:
        print(f"{colors['red']}You didn´t enter any number 3{colors['clean']}")
    else:
        print(f"{colors['blue']}You enter {tuple.count(3)} {'numbers' if tuple.count(3) > 1 else 'number'} 3 and the first place is {tuple.index(3)}{colors['clean']}")
    if tuple.count(9) == 0:
        print(f"{colors['red']}You didn´t enter any number 9{colors['clean']}")
    else:
        print(f"{colors['blue']}You enter {tuple.count(9)} {'numbers' if tuple.count(9) > 1 else 'number'} 9{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
