colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
from datetime import date
y = int(input("Type any year and if you just wanna write the actual year type 0: "))
if y == 0:
    y = date.today().year
if (y % 4) == 0 and (y % 100) != 0 or (y % 400) == 0:
    print("\033[32m{} is a leap year\033[m".format(y))
else:
    print("\033[31m {} isn´t a leap year\033[m".format(y))
