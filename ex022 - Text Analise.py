from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Hello, please tell me your name: ")).strip()
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
print("your name with all letter up is {}{}{}"
      "\nAnd with all letters lower is {}{}{}"
      .format(colors["cian"], name.upper(), colors["clean"],
              colors["yellow"], name.lower(), colors["clean"]))
division = name.split()
print("Your name has {}{}{} letters"
      "\nYour first name is {}{}{} and has {}{}{} letters"
      .format(colors["green"], len(name) - name.count(" "), colors["clean"],
              colors["green"], division[0], colors["clean"],
              colors["green"], len(division[0]), colors["clean"]))
if len(name) - name.count(" ") > 25:
    print("{}Omg your is very big{}".format(colors["red"], colors["clean"]))
if division[0] == "Miguel":
    print("{}Your name is very cool, congratulations!!!{}".format(colors["purple"], colors["clean"]))
print("Nice to meet you {}{}{}".format(colors["blue"], name, colors["clean"]))
