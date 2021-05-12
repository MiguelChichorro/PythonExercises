from datetime import date
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
y = int(input("Enter any year and if you just wanna write the actual year Enter 0: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if y == 0:
    y = date.today().year
if (y % 4) == 0 and (y % 100) != 0 or (y % 400) == 0:
    print("{}{} is a leap year{}".format(colors["green"], y, colors["clean"]))
else:
    print("{}{} isn´t a leap year{}".format(colors["red"], y, colors["clean"]))
