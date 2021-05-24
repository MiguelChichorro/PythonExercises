from time import sleep
from random import randint
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
print("{}<--------------------------------->{}".format(colors["yellow"], colors["clean"]))
print("{}\U0001F916 I WANNA PLAY A GAME!!!!! \U0001F916{}".format(colors["blue"], colors["clean"]))
print("{}<--------------------------------->{}".format(colors["yellow"], colors["clean"]))
print("{}HMMMM I choose a number between 0 and 10{}".format(colors["yellow"], colors["clean"]))
while ans == 1:
    cont = 0
    com = randint(0, 10)
    player = int(input("{}\U0001F914 What is the number I choose \U0001F914?{} ".format(colors["blue"], colors["clean"])))
    print("{}Loading...{}".format(colors["green"], colors["clean"]))
    sleep(2)
    while player != com:
        player = int(input("{}Hmmm you missed{}\nTry again:  ".format(colors["red"], colors["clean"])))
        cont += 1
    print("{}={}".format(colors["green"], colors["clean"]) * 20)
    print("{}\U0001F973\U0001F973\U0001F973\U0001F973{}".format(colors["green"], colors["clean"]))
    print("{}CONGRADULATIONS{}, {}YOU DISCOVERED THE NUMBER{}"
          .format(colors["green"], colors["clean"],
                  colors["blue"], colors["clean"]))
    print("{}I choose the number {}{}{} and you found"
          .format(colors["green"], colors["yellow"], com, colors["green"],))
    if cont == 0:
        print("{}\U0001F913 You just needed an attempt, you´re very smart \U0001F913{}".format(colors["green"], colors["clean"]))
    elif (cont > 0) and (cont < 5):
        print("{}\U0001F60E You needed {} {}, nice \U0001F60E{}".format(colors["purple"], cont, "attempt" if cont == 1 else "attemps", colors["clean"]))
    elif (cont > 5) and (cont < 9):
        print("{}\U0001F642 You needed {} attempts, it´s ok \U0001F642{}".format(colors["yellow"], cont, colors["clean"]))
    else:
        print("{}\U0001F610 Omg you needed a lot of attempts \U0001F610{}".format(colors["red"], colors["clean"]))
    ans = int(input("{}Do you wanna play again? \nPress [1] to play again or another number to leave:{} "
                    .format(colors["blue"], colors["clean"], colors["yellow"], colors["clean"])))
if ans != 1:
    print("{}<--------------------------------->{}".format(colors["yellow"], colors["clean"]))
    print("{}\U0001F916 GAME OVER \U0001F916{}".format(colors["blue"], colors["clean"]))
    print("{}<--------------------------------->{}".format(colors["yellow"], colors["clean"]))
