colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
for c in range(1, 51):
    if(c % 2) == 0:
        print("|| {}{:2}{} ||".format(colors["blue"], c, colors["clean"]))
