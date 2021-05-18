from random import sample
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
order = ["Rafael", "Hugo", "Miguel", "Edvaldo"]
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
print("The presentation order is {}{}{} "
      .format(colors["yellow"], sample(order, k=4), colors["clean"]))
