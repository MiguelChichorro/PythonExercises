from time import sleep
from playsound import playsound
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
number = int(input("Enter any number int between 0 and 9999: "))
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
if number > 9999:
    print("{}You need to Enter a number smaller 9999{}".format(colors["red"], colors["clean"]))
else:
    u = number // 1 % 10
    t = number // 10 % 10
    h = number // 100 % 10
    th = number // 1000 % 10
    print("{}Unity: {}{}"
          "\n{}Tens: {}{}"
          "\n{}Hundreds: {}{}"
          "\n{}Thousand: {}{}"
          .format(colors["yellow"], u, colors["clean"],
                  colors["blue"], t, colors["clean"],
                  colors["purple"], h, colors["clean"],
                  colors["red"], th, colors["clean"]))
    if number == 115:
        print("{}Congratulations!!! You find the blood of the dead song{}".format(colors["cian"], colors["clean"]))
        playsound('../../Implements/zbs.mp3')
