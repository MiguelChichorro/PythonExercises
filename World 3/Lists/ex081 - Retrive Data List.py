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
    cont5 = 0
    while True:
        ans2 = ""
        print(f"{colors['yellow']}If you want to stop just enter 0{colors['clean']}")
        n = int(input("Enter a number: "))
        values.append(n)
        if n == 5:
            cont5 += 1
        if 0 in values:
            values.remove(0)
            values.sort(reverse=True)
            break
    print(f"{colors['green']}Your list have {len(values)} {'just one number' if len(values) == 1 else 'numbers'}{colors['clean']}")
    while ans2 != "N" and ans2 != "R":
        ans2 = str(input(f"{colors['blue']}You want to see your list in reverse or normal form? [N/R]: {colors['clean']}")).upper()
    if ans2 == "N":
        values.sort()
        print(f"{colors['yellow']}Your list sorted is {values}{colors['clean']}")
    else:
        values.sort(reverse=True)
        print(f"{colors['yellow']}Your list reverse sorted is {values}{colors['clean']}")
    if cont5 == 0:
        print(f"{colors['red']}You don´t enter any time the number 5{colors['clean']}")
    else:
        print(f"{colors['green']}You enter the number five {cont5} {'time' if cont5 == 1 else 'times'} in the postions", end=" ")
        for i, v in enumerate(values):
            if v == 5:
                print(f"{i}...", end="")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
