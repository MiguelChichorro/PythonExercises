from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Type your name please: ")).strip()
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
print("Nice to meet you {}{}{}".format(colors["blue"], name, colors["clean"]))
name = name.split()
print("First name {}{}{}"
      "\nLast name {}{}{}"
      .format(colors["blue"], name[0], colors["clean"],
              colors["blue"], name[-1], colors["clean"]))
