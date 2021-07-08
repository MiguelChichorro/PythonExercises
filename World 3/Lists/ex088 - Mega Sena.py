from time import sleep
from random import sample
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    games = list()
    print(f"{colors['purple']}={colors['clean']}" * 27)
    print(f"{colors['purple']}{'MEGA SENA': ^45}{colors['clean']}")
    print(f"{colors['purple']}={colors['clean']}" * 27)
    op = int(input("How many tips do you want? "))
    print('-=-' * 3, " LOADING ", '-=-' * 3)
    for game in range(0, op):
        tip = sample(range(60), 6)
        tip.sort()
        games.append(tip[:])
        tip.clear()
    for i, l in enumerate(games):
        sleep(0.5)
        print(f"{colors['green']}Game {i+1}: {l}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
