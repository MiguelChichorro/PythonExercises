from time import sleep
from random import randint
from operator import itemgetter
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
players = {'Player 1': randint(1, 6),
           'Player 2': randint(1, 6),
           'Player 3': randint(1, 6),
           'Player 4': randint(1, 6)}
ranking = list()
print(f"{colors['yellow']}Press Enter to start{colors['clean']}")
for k, v in players.items():
    sleep(0.5)
    print(f"The {k} got {v}")
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
sleep(1)
print("=" * 30)
print("  ==  PLAYER RANKING  ==  ")
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f"{i + 1}° place: {v[0]} with {v[1]} points.")
