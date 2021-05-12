from datetime import date
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Enter your name: "))
day = int(input("Enter the your birth day: "))
month = int(input("Enter the your birth month: "))
year = int(input("Enter the your birth year: "))
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
birth = date(year, month, day)
today = date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
print("{}You are {} years old{}".format(colors["blue"], age, colors["clean"]))
if age <= 9:
    print("{}You are Mirin{}".format(colors["blue"], colors["clean"]))
elif (age > 9) and (age <= 14):
    print("{}You are Childish{}".format(colors["cian"], colors["clean"]))
elif (age > 14) and (age <= 19):
    print("{}You are Junior{}".format(colors["purple"], colors["clean"]))
elif (age > 19) and (age <= 20):
    print("{}You are Sênior{}".format(colors["yellow"], colors["clean"]))
elif (age > 20) and (age <= 100):
    print("{}You are Master{}".format(colors["red"], colors["clean"]))
else:
    print("{}You are Legend{}".format(colors["green"], colors["clean"]))
