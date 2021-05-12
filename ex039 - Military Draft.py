from datetime import date
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Type your name: "))
day = int(input("Type the your birth day: "))
month = int(input("Type the your birth month: "))
year = int(input("Type the your birth year: "))
birth = date(year, month, day)
today = date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if age == 17 or age == 18:
    print("{}Hello {}"
          "\nYou have {} years old"
          "\nYou need to enlist this year{}"
          .format(colors["yellow"], name, age, colors["clean"]))
elif age < 17:
    y = 17 - age
    print("{}Hello {}"
          "\nYou have {} years old"
          "\nYou need to enlist in {} years{}"
          .format(colors["blue"], name, age, y, colors["clean"]))
else:
    y = age - 18
    print("{}Hello {}"
          "\nYou have {} years old"
          "\nYour enlistment time was {} years ago{}"
          .format(colors["red"], name, age, y, colors["clean"]))
