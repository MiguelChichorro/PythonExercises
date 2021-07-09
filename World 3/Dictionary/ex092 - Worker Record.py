from time import sleep
from datetime import date
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    person = dict()
    person['name'] = str(input("Enter your name: "))
    day = int(input("Enter the your birth day: "))
    month = int(input("Enter the your birth month: "))
    year = int(input("Enter the your birth year: "))
    birth = date(year, month, day)
    today = date.today()
    person['age'] = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print(f"{colors['red']}If you don´t have a CTPS Enter 0{colors['clean']}")
    person['ctps'] = int(input("Enter you CTPS number: "))
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    if person['ctps'] != 0:
        apo = int(input("What year did you start to work?"))
        person['Retirement'] = ((35 - (today.year - apo)) + person['age'])
        person['salary'] = int(input("Enter your salary: R$"))
        print(f"{colors['blue']}Reading data...{colors['clean']}")
        sleep(1)
    for k, v in person.items():
        print(f"{colors['purple']}Your {k} is {v}{colors['clean']}")
    if person['ctps'] == 0:
        print(f"{colors['red']}You don´t work yet{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
