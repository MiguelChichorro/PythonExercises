from math import trunc
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Enter a real number: "))
print("Your number is {}{:.2f}{} and using the function trunc is {}{}{}"
      "\nBut we can use the function int to {}{}{}"
      "\n{}the two doing the same thing{}"
      .format(colors["cian"], n1, colors["clean"],
              colors["cian"], trunc(n1), colors["clean"],
              colors["cian"], int(n1), colors["clean"],
              colors["green"], colors["clean"]))
