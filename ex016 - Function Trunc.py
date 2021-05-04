colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
from math import trunc
n1 = float(input("Type a real number: "))
print("Your number is {:.2f} and using the function trunc is {} \nBut we can use the function int to {}".format(n1, trunc(n1), int(n1)))
