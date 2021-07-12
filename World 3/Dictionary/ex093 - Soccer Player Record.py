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
    matches = list()
    player = dict()
    sumtotal = 0
    player['name'] = str(input("Enter your name: "))
    player['match'] = int(input("How many matches did you play? "))
    for c in range(0, player['match']):
        n = int(input(f"how many goals did you do in the {c + 1}° match? "))
        sumtotal += n
        matches.append(n)
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("=" * 30)
    print(f"{colors['yellow']}Hello {player['name']}{colors['clean']}")
    print(f"{colors['yellow']}You played {player['match']} {'match' if player['match'] == 1 else 'matches'} in this championship{colors['clean']}")
    for c, v in enumerate(matches):
        print(f"{colors['yellow']}In the {c + 1}° match you did {v} goals{colors['clean']}")
    print(f"{colors['yellow']}You did {sumtotal} {'goal' if sumtotal == 1 else 'goals'} this championship{colors['clean']}")
    print("=" * 30)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
