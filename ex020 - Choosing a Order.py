colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
from random import sample
order = ["Rafael", "Hugo", "Miguel", "Edvaldo"]
print("The presentation order is {} ".format(sample(order, k=4)))
