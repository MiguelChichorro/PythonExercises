from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def token(a='<invisible>', b=0):
    if a == '':
        a = '<invisible>'
    print(f"{colors['yellow']}The player {a} did {b} {'goal' if b == 1 else 'goals'}{colors['clean']}")


name = str(input("Enter the name: "))
goal = str(input("How many goals did you do? "))
print(f"{colors['purple']}Reading data...{colors['clean']}")
sleep(1)
if goal.isnumeric():
    goal = int(goal)
else:
    goal = 0
if name.strip() == " ":
    token(b=goal)
else:
    token(name, goal)
