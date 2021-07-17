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
    people = list()
    person = dict()
    contperson = sumtotal = contgirl = 0
    while True:
        person['name'] = str(input("Enter your name: "))
        person['gender'] = str(input(f"Enter your gender. \n{colors['blue']}[M]{colors['clean']} or {colors['purple']}[F]{colors['clean']}: ")).strip().upper()[0]
        while person['gender'] != "M" and person['gender'] != "F":
            person['gender'] = str(input(f"{colors['red']}Enter your gender. \n{colors['blue']}[M]{colors['clean']} or {colors['purple']}[F]{colors['clean']}: ")).strip().upper()[0]
        if person['gender'] == "F":
            contgirl += 1
        day = int(input("Enter the your birth day: "))
        month = int(input("Enter the your birth month: "))
        year = int(input("Enter the your birth year: "))
        birth = date(year, month, day)
        today = date.today()
        person['age'] = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        sumtotal += person['age']
        contperson += 1
        people.append(person.copy())
        ans = str(input(
            f"Do you want do add another person? [{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[
            0]
        while ans != "Y" and ans != "N":
            ans = str(input(
                f"{colors['red']}Please just enter Yes or No {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[
                0]
        if ans == "N":
            break
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    avg = sumtotal/contperson
    print("=" * 30)
    print(f"{colors['green']}{contperson} {'peoples' if contperson > 1 else 'person'} were registered{colors['clean']}")
    print(f"{colors['green']}The average age is {avg:5.2f}{colors['clean']}")
    if contgirl > 0:
        print(f"The Women registred are", end=" ")
        for c in people:
            if c['gender'] in "F":
                print(f"{c['name']}", end=" ")
        print()
    else:
        print(f"{colors['red']}Any Woman was enter{colors['clean']}")
    for c in people:
        if c['age'] >= avg:
            for k, v in c.items():
                print(f'{k} = {v}; ', end=" ")
            print()
    print("=" * 30)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
