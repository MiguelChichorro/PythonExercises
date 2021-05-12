colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input("Enter a number: "))
print("Your number is {}{}{}, "
      "\nThe successor of your number is {}{}{}"
      "\nAnd the predecessor is {}{}{}"
      .format(colors["blue"], n1, colors["clean"],
              colors["blue"], n1+1, colors["clean"],
              colors["blue"], n1-1, colors["clean"]))
