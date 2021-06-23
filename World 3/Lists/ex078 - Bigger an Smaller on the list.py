from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
values = list()
for c in range(0, 5):
    values.append(int(input(f"Enter a number to the position {c}: ")))
print(f"{colors['blue']}Reading data...{colors['clean']}")
sleep(1)
print(f"{colors['green']}The bigger value is {max(values)} and you find him in the positions", end=" ")
for c, v in enumerate(values):
    if v == max(values):
        print(f"{c}...", end="")
print(f"\n{colors['yellow']}The smaller value is {min(values)} and you find him in the positions", end=" ")
for i, v in enumerate(values):
    if v == min(values):
        print(f"{i}...", end="")
