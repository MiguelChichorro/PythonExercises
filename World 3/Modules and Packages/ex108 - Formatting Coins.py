import ultilities
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n = int(input("Enter How much money do you want to converse: R$"))
print(f"{colors['purple']}Reading data...{colors['clean']}")
sleep(1)
print(f"{colors['blue']}The double is {ultilities.coin(ultilities.double(n))}{colors['clean']}")
print(f"{colors['yellow']}The half is {ultilities.coin(ultilities.half(n))}{colors['clean']}")
print(f"{colors['red']}The up is {ultilities.coin(ultilities.up(n))}{colors['clean']}")
print(f"{colors['purple']}The down is {ultilities.coin(ultilities.down(n))}{colors['clean']}")
