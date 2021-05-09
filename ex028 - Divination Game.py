from random import randint
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = randint(1, 5)
print("{}==={}".format(colors["yellow"], colors["clean"]) * 6)
print("{}LET´S PLAY A GAME!!!{}".format(colors["purple"], colors["clean"]))
print("{}==={}".format(colors["yellow"], colors["clean"]) * 6)
answer = int(input("Choose a number between 0 and 5: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if answer == num:
    print("{}Congratulations, you win :D{}".format(colors["green"], colors["clean"]))
else:
    print("{}hmm sorry try again later ;---------;{}".format(colors["red"], colors["clean"]))
print("{}GAME OVER!!! The game number is {} and your number is {}{}"
      .format(colors["cian"], num, answer, colors["clean"]))
