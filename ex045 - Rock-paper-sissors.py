from random import randint
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
itens = ("ROCK", "PAPER", "SISSORS")
com = randint(0, 2)
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
print("{}LET´S PLAY ROCK-PAPER-SISSORS!!!{}".format(colors["red"], colors["clean"]))
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
player = int(input("{}Come enter\n[ 0 ] PAPER\n[ 1 ] ROCK\n[ 2 ] SISSORS\nWhat´s your choice: {}".format(colors["cian"], colors["clean"])))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("{}-=-{}".format(colors["blue"], colors["clean"]) * 7)
print("{}You choose {}\nthe computer choose {}{}".format(colors["yellow"], itens[player], itens[com],  colors["clean"]))
print("{}-=-{}".format(colors["blue"], colors["clean"]) * 7)
if player == 0 and com == 1:
    print("{}Congradulations you ate the computer :D{}".format(colors["green"], colors["clean"]))
elif com == 0 and player == 1:
    print("{}Sorry but you were ate;------;{}".format(colors["red"], colors["clean"]))
elif player == 1 and com == 2:
    print("{}Congradulations you smashed the computer :D{}".format(colors["green"], colors["clean"]))
elif com == 1 and player == 2:
    print("{}Sorry but you were smashed;------;{}".format(colors["red"], colors["clean"]))
elif player == 2 and com == 0:
    print("{}Congradulations you cut the computer :D{}".format(colors["green"], colors["clean"]))
elif com == 2 and player == 0:
    print("{}Sorry but you were cut;------;{}".format(colors["red"], colors["clean"]))
elif com == player:
    print("{}Luckily for us this round drew{}".format(colors["purple"], colors["clean"]))
else:
    print("{}You need to right only Paper, Sissors or Rock{}".format(colors["red"], colors["clean"]))
    print("{}Try Again{}".format(colors["red"], colors["clean"]))

print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
print("{}GAME OVER!!!{}".format(colors["red"], colors["clean"]))
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)


