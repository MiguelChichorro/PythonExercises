from time import sleep
from datetime import date
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def vote(years):
    if years < 18:
        return print(f"{colors['green']}{years} don´t need to vote{colors['clean']}")
    elif years >= 18:
        return print(f"{colors['red']}{years} need to vote{colors['clean']}")
    elif years >= 65:
        return print(f"{colors['yellow']}{years} can vote if the person want{colors['clean']}")


day = int(input("Enter the your birth day: "))
month = int(input("Enter the your birth month: "))
year = int(input("Enter the your birth year: "))
birth = date(year, month, day)
today = date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
print(f"{colors['purple']}Reading data...{colors['clean']}")
sleep(1)
print("=" * 30)
vote(age)
