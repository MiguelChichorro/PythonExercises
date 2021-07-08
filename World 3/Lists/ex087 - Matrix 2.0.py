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
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sumall = scol = 0
    for l in range(0, 3):
        for c in range(0, 3):
            m[l][c] = int(input("Enter a number: "))
            if m[l][c] % 2 == 0:
                sumall += m[l][c]
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("-=-" * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f"{colors['blue']}[ {m[l][c]} ]{colors['clean']}", end=" ")
        print()
    print(f"{colors['purple']}The even sum is {sumall}{colors['clean']}")
    print(f"{colors['purple']}The bigger value in the line 2 is {max(m[1])}{colors['clean']}")
    for l in range(0, 3):
        scol += m[l][2]
    print(f"{colors['purple']}The all values in the line 3 sum is {scol}{colors['clean']}")
    print("-=-" * 30)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
