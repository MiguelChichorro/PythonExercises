from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ph = str(input("Type any phrase here: ")).upper().strip()
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
print("The phrase has {}{}{} letters {}A{}".format(colors["yellow"], ph.count("A"), colors["clean"], colors["yellow"], colors["clean"]))
sleep(1)
print("The first position is {}{}{}".format(colors["yellow"], ph.find("A")+1, colors["clean"]))
sleep(1)
print("And the last is {}{}{}".format(colors["yellow"], ph.rfind("A")+1,  colors["clean"]))
sleep(1)
print("Your phrase is {}{}{}".format(colors["yellow"], ph, colors["clean"]))
