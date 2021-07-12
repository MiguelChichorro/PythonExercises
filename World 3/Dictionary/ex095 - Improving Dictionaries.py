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
    team = list()
    matches = list()
    player = dict()
    sumtotal = 0
    while True:
        player.clear()
        player['name'] = str(input("Enter your name: "))
        tot = int(input("How many matches did you play?"))
        matches.clear()
        for c in range(0, tot):
            matches.append(int(input(f"How many goals did you do in the {c + 1}° match? ")))
        player['goals'] = matches[:]
        player['total'] = sum(matches)
        team.append(player.copy())
        ans = str(input(
            f"Do you want do add another person? [{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[
            0]
        while ans != "Y" and ans != "N":
            ans = str(input(
                f"{colors['red']}Please just enter Yes or No [{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[
                0]
        if ans == "N":
            break
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("=" * 30)
    print('Cod', end=" ")
    for i in player.keys():
        print(f"{i:<15}", end=" ")
    print()
    for i, v in enumerate(team):
        print(f"{i:<7}", end=" ")
        for d in v.values():
            print(f"{str(d):<15}", end=" ")
        print()
    while True:
        print("-" * 57)
        print(f"{colors['red']}if you want to stop just enter 999{colors['clean']}")
        n = int(input("Enter a number:"))
        if n == 999:
            print(f"{colors['red']}Stoping...{colors['clean']}")
            break
        if n <= len(team) - 1:
            print(f"{colors['green']}the {team[n]['name']} goals are:{colors['clean']}")
            for i, g in enumerate(team[n]['goals']):
                print(f"    in the {i + 1}° game did {g} {'goal' if g == 1 else 'goals'}")
        else:
            print(f"{colors['red']}This player dosen´t exist{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")