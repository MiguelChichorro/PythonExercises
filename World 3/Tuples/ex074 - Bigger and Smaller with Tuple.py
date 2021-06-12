from random import randint
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
    for c in range(5):
        n = randint(1, 9)
        tuple += n,
    print(f"{colors['green']}The values are: {sorted(tuple)}{colors['clean']}")
    print(f"{colors['green']}The bigger value was {max(tuple)}{colors['clean']}")
    print(f"{colors['green']}The smaller value was {min(tuple)}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
