from math import sin, cos,  tan, radians
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Enter a number :"))
Sin = sin(radians(n1))
Cos = cos(radians(n1))
Tan = tan(radians(n1))
print("{}Your number is {}{}"
      "\n{}Your SIN is {:.2f}{}"
      "\n{}Your COS {:.2f}{}"
      "\n{}The last is TAN the yours is {:.2f}{}"
      .format(colors["cian"], n1, colors["clean"],
              colors["purple"], Sin, colors["clean"],
              colors["cian"], Cos, colors["clean"],
              colors["purple"], Tan, colors["clean"]))
