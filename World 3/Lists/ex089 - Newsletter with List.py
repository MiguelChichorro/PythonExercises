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
    students = list()
    ans2 = 'Y'
    while ans2 == 'Y':
        name = str(input("Enter a name:"))
        n1 = int(input("Entear a mark: "))
        n2 = int(input("Enter a mark: "))
        avg = (n1 + n2) / 2
        students.append([name, [n1, n2], avg])
        ans2 = str(input("Want continue? [Y/N]")).upper()
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("-=" * 20)
    print(f"{'NU.':<8}{'NAME':<20}{'AVG':<16}")
    print("-" * 37)
    for i, a in enumerate(students):
        print(f"{i:<8}{a[0]:<25}{a[2]:<8.1f}")
    print("-" * 37)
    while True:
        print(f"{colors['red']}if you want to stop just enter 999{colors['clean']}")
        n = int(input("Enter a number:"))
        if n <= len(students) - 1:
            if n == 999:
                print(f"{colors['red']}Stoping...{colors['clean']}")
                break
            print(f"{colors['green']}the {students[n][0]} marks are {students[n][1]}{colors['clean']}")
            print(f"{colors['green']}AGAIN{colors['clean']}")
        else:
            print(f"{colors['red']}This student dosen´t exist{colors['clean']}")
            print(f"{colors['red']}COMEBACK{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
