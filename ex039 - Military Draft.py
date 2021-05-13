from datetime import date
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
gender = int(input("Before continuing the enlistment Enter your gender""\n [ 1 ] Man" "\n [ 2 ] Woman\n: "))
if gender == 2:
    print("Yo aren´t required to do the enlistment")
    print("Have a good day")
elif gender == 1:
    name = str(input("Enter your name: "))
    day = int(input("Enter the your birth day: "))
    month = int(input("Enter the your birth month: "))
    year = int(input("Enter the your birth year: "))
    birth = date(year, month, day)
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print("{}reading data...{}".format(colors["green"], colors["clean"]))
    sleep(0.5)
    if age == 18:
        print("{}Hello {}"
              "\nYou have {} years old"
              "\nYou need to enlist this year{}"
              .format(colors["yellow"], name, age, colors["clean"]))
    elif age < 18:
        y = 18 - age
        year = date.today().year + y
        print("{}Hello {}"
              "\nYou have {} years old"
              "\nYou need to enlist in {} {} in {}{}"
              .format(colors["green"], name, age, y, "years" if y > 1 else "year", year, colors["clean"]))
    else:
        y = age - 18
        year = date.today().year - y
        print("{}Hello {}"
              "\nYou have {} years old"
              "\nYour enlistment time was {} {} ago in {}{}"
              .format(colors["red"], name, age, y, "years" if y > 1 else "year", year, colors["clean"]))
    if (today.month == birth.month) and (today.day == birth.day):
        print("{}Happy birthday to you!!!{}"
              "\n{}Happy birthday to you!!!{}"
              "\n{}Happy birthday to you!!!{}"
              .format(colors["yellow"], colors["clean"], colors["cian"], colors["clean"], colors["purple"],
                      colors["clean"]))
else:
    print("{}Please enter 1 or 2 only{}".format(colors["red"], colors["clean"]))
