from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    students = dict()
    school = list()
    ans2 = 'Y'
    while ans2 == 'Y':
        students['name'] = str(input("Enter your name: "))
        n1 = int(input("Enter the first mark: "))
        n2 = int(input("Enter the second mark: "))
        students['avg'] = (n1 + n2) / 2
        if students['avg'] >= 6:
            students['stats'] = f'{colors["green"]}Approved{colors["clean"]}'
        else:
            students['stats'] = f'{colors["red"]}Disapproved{colors["clean"]}'
        school.append(students.copy())
        ans2 = str(input("Want continue? [Y/N]")).upper()
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("=" * 30)
    print(f"{'NAME':<20}{'AVG':<18}{'STATS':<17}")
    print("=" * 30)
    for e in school:
        for c in e.values():
            print(f"{c:<20}", end=" ")
        print()
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
