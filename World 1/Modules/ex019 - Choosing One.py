from random import choice
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
student = ["Rafael", "Hugo", "Miguel", "Edvaldo"]
print("{}Hmm...{}".format(colors["red"], colors["clean"]))
sleep(2)
print("The student chosen is {}{}{}".format(colors["green"], choice(student), colors["clean"]))
