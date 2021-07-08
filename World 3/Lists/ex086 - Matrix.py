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
    for l in range(0, 3):
        for c in range(0, 3):
            m[l][c] = int(input(f"Enter a number for [{l}, {c}]: "))
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f"[ {m[l][c]} ]", end=" ")
        print()
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
