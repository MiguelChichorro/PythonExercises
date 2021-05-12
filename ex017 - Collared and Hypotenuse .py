from math import hypot
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ca = float(input("Enter the value of the adjacent over: "))
co = float(input("Enter the value of the opposite over: "))
hyp = hypot(co, ca)
print(" The adjacent over is {}{:.2f}{} and the opposite over is {}{:.2f}{} "
      "\n Doing the count we have {}{:.2f}{} like Hypotenuse"
      .format(colors["purple"], ca, colors["clean"],
              colors["purple"], co, colors["clean"],
              colors["purple"], hyp, colors["clean"]))
