from time import sleep
from playsound import playsound
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("{}\U0001F4A5{}".format(colors["yellow"], colors["clean"]) * 10)
print("{}BOOM{} ".format(colors["blue"], colors["clean"]) * 3)
print("{}\U0001F4A5{}".format(colors["red"], colors["clean"]) * 10)
playsound('Implements\\champions.mp3')
