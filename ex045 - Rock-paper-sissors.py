from random import choice
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
com = ["ROCK", "PAPER", "SISSORS"]
com = choice(com)
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
print("{}LET´S PLAY ROCK-PAPER-SISSORS!!!{}".format(colors["red"], colors["clean"]))
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
sleep(0.5)
print("{}Let´s begin{}".format(colors["yellow"], colors["clean"]))
player = str(input("{}Come enter with what you choose: {}".format(colors["cian"], colors["clean"])))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
player = player.upper()
print("{}You choose {} and the computer choose {}{}".format(colors["yellow"], player, com,  colors["clean"]))
if player == "PAPER" and com == "ROCK":
    print("{}Congradulations you ate the computer :D{}".format(colors["green"], colors["clean"]))
elif com == "PAPER" and player == "ROCK":
    print("{}Sorry but you were ate;------;{}".format(colors["red"], colors["clean"]))
elif player == "ROCK" and com == "SISSORS":
    print("{}Congradulations you smashed the computer :D{}".format(colors["green"], colors["clean"]))
elif com == "ROCK" and player == "SISSORS":
    print("{}Sorry but you were smashed;------;{}".format(colors["red"], colors["clean"]))
elif player == "SISSORS" and com == "PAPER":
    print("{}Congradulations you cut the computer :D{}".format(colors["green"], colors["clean"]))
elif com == "SISSORS" and player == "PAPER":
    print("{}Sorry but you were cut;------;{}".format(colors["red"], colors["clean"]))
elif com == player:
    print("{}Luckily for us this round drew{}".format(colors["purple"], colors["clean"]))
else:
    print("{}You need to right only Paper, Sissors or Rock{}".format(colors["red"], colors["clean"]))
    print("{}Try Again{}".format(colors["red"], colors["clean"]))
sleep(2)
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)
print("{}GAME OVER!!!{}".format(colors["red"], colors["clean"]))
print("{}==={}".format(colors["cian"], colors["clean"]) * 10)


