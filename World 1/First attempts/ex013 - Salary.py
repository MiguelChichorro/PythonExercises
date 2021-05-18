colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
oldsal = float(input("Enter your old salary: R$ "))
newsal = oldsal + (oldsal * 0.15)
print("Your old salary is {}R${:.2f}{}"
      "\nAnd your new salary with 15% increase is {}R${:.2f}{}"
      .format(colors["red"], oldsal, colors["clean"],
              colors["green"], newsal, colors["clean"]))
