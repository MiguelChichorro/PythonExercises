colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Type the first grade: "))
n2 = float(input("Type the second grade:"))
n3 = float(input("Type the thirty grade "))
avg = (n1 + n2 + n3) / 3
print("Your first grade was {}{}{}"
      "\nYour second grade was {}{}{}"
      "\nAnd your last grade was {}{}{}"
      .format(colors["cian"], n1, colors["clean"],
              colors["cian"], n2, colors["clean"],
              colors["cian"], n3, colors["clean"]))
if avg < 6:
    print("{}The average you got on the two months is {:.1f}"
          "\nSorry but you need to do the test again{}"
          .format(colors["red"], avg, colors["clean"]))
else:
    print("{}The average you got on the two months is {:.1f}"
          "\nCongratulations you pass!!! {}"
          .format(colors["green"], avg, colors["clean"]))
