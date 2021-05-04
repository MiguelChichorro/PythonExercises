colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
from math import hypot
ca = float(input("Type the value of the adjacent over: "))
co = float(input("Type the value of the opposite over: "))
'''hyp = (pow(ca, 2) + pow(co, 2)) ** (1/2)'''
hyp = hypot(co, ca)
print(" The adjacent over is {:.2f} and the opposite over is {:.2f} \n Doing the count we have {:.2f} like Hypotenuse".format(ca, co, hyp))
