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
    mcont = wcont= wagecont = cont = agecont = 0
    while True:
        name = gender = ""
        age, ans2 = 0, 1
        print("=" * 20)
        name = str(input("Enter the name: "))
        age = int(input("Enter the birth year: "))
        age = date.today().year - age
        gender = str(input(f"Enter your gender. \n{colors['blue']}[M]{colors['clean']} or {colors['purple']}[F]{colors['clean']}: ")).strip().upper()[0]
        while gender != "M" and gender != "F":
            gender = str(input(f"{colors['red']}Please enter just {colors['blue']}M{colors['clean']} or {colors['purple']}F{colors['clean']}: ")).strip().upper()[0]
        cont += 1
        if gender == "M":
            mcont += 1
            print(f"{colors['blue']}Welcome lord {name}{colors['clean']}")
            print(f"{colors['blue']}Gender: {gender}\nAge:{age}{colors['clean']}")
            print("=" * 20)
        elif gender == "F":
            wcont += 1
            print(f"{colors['purple']}Welcome lady {name}{colors['clean']}")
            print(f"{colors['purple']}Gender: {gender}\nAge:{age}{colors['clean']}")
            print("=" * 20)
        if age >= 18:
            agecont += 1
        if gender == "F" and age >= 20:
            wagecont += 1
        ans2 = int(input(f"{colors['green']}\nPress [ 1 ] to enter another person or another number to leave: {colors['clean']}"))
        if ans2 != 1:
            break
    print(f"{colors['yellow']}You enter {cont} {'person' if cont == 1 else 'people'} and {'only one person is over ' if cont == 1 else f'{agecont} people are over '}18 years old{colors['clean']}")
    if mcont == 0:
        print("You do not enter men")
    else:
        print(f"{colors['blue']}You enter {'Just one man' if mcont == 1 else f'{mcont} men'}{colors['clean']}")
    if wcont == 0:
        print("You do not enter women")
    else:
            if wagecont == 0:
                print(
                    f"{colors['purple']}You enter {'Just one woman and she is not over 20 yeas old' if wcont == 1 else f'{wcont} women and they are not over 20 yeas old'}{colors['clean']}")
            else:
                print(
                    f"{colors['purple']}You enter {'Just one woman and she is over 20 yeas old' if wcont == 1 else f'{wcont} women and they are over 20 yeas old'}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
