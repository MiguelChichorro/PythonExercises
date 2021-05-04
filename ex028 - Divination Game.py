colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
from random import randint
from time import sleep
num = randint(1, 5)
print("\033[33m===\033[m" * 6)
print("\033[36mLET´S PLAY A GAME!!!\033[m")
print("\033[33m===\033[m" * 6)
answer = int(input("Choose a number between 0 and 5: "))
print("\033[35mHmm let´s see...\033[m")
sleep(2)
if answer == num:
    print("\033[32mCongratulations, you win :D\033[m")
else:
    print("\033[31mhmm sorry try again later ;---------;\033[m")
print("\033[34mGAME OVER!!! The game number is {} and your number is {}\033[m".format(num, answer))
