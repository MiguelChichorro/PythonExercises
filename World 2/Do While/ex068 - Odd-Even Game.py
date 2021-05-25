from random import randint, choice
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
choices = ["ODD", "EVEN"]
ans = 1
while ans == 1:
    cont = 0
    print(F"{colors['blue']}={colors['clean']}" * 20)
    print(F"{colors['yellow']}LET´S PLAY ODD-EVEN{colors['clean']}")
    print(F"{colors['blue']}={colors['clean']}" * 20)
    while True:
        sum = 0
        comc = choice(choices)
        print(f"{colors['yellow']}I choose {comc}{colors['clean']}")
        comn = randint(1, 10)
        player = int(input("What´s your number: "))
        sum = player + comn
        sleep(1)
        print("ODD")
        sleep(1)
        print("EVEN!!!")
        sleep(1)
        print("The sum issss")
        sleep(1)
        print(f"{sum} {'IS EVEN' if (sum % 2) == 0 else 'IS ODD'}")
        if "EVEN" in comc and (sum % 2) == 0:
            break
        elif "ODD" in comc and (sum % 2) != 0:
            break
        else:
            cont += 1
            print(f"{colors['green']}AFFF YOU WIN BUT NEXT TIME I´M GOING TO WIN{colors['clean']}")
    print(f"{colors['red']}I WIN UHUUUUUU, you won {cont} {'time' if cont == 1 else 'times'}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to play again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(F"{colors['blue']}={colors['clean']}" * 20)
    print(F"{colors['yellow']}GAME OVER{colors['clean']}")
    print(F"{colors['blue']}={colors['clean']}" * 20)
