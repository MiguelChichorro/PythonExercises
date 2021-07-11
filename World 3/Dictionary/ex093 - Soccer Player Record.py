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
    player = dict()
    sumtotal = 0
    player['name'] = str(input("Enter your name: "))
    player['rounds'] = int(input("How many rounds do you played? "))
    for c in range(0, player['rounds']):
        n = int(input(f"how many gols did you do in the {c + 1}° round? "))
        sumtotal += n
    print(f"{colors['blue']}Reading data...{colors['clean']}")
    sleep(1)
    print("=" * 30)
    print(f"{colors['yellow']}Hello {player['name']}{colors['clean']}")
    print(f"{colors['yellow']}You played {player['rounds']} {'round' if player['rounds'] == 1 else 'rounds'} in this championship{colors['clean']}")
    print(f"{colors['yellow']}You did {sumtotal} {'gol' if sumtotal == 1 else 'gols'} this championship{colors['clean']}")
    print("=" * 30)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
