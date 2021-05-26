colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    while True:
        n = c = result = 0
        n = int(input("Enter a number to the table :"))
        if n < 0:
            break
        print("=" * 15)
        for c in range(0, 11):
            result = c * n
            print(f"{colors['blue']}{n} * {c} = {result}{colors['clean']}")
        print("=" * 15)
    if n < 0:
        print(f"{colors['red']}Closed program{colors['clean']}")
        ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
