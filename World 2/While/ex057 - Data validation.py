colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
gender = str(input("Enter your gender. \n{}[M]{} or {}[F]{}: "
                   .format(colors["blue"], colors["clean"], colors["purple"], colors["clean"]))).strip().upper()[0]
while gender != "M" and gender != "F":
    gender = str(input("{}Please enter just {}M{} or {}F{}: "
                       .format(colors["red"], colors["blue"], colors["clean"], colors["purple"], colors["clean"]))).strip().upper()[0]
if gender == "M":
    print("{}Welcome, Lord{}".format(colors["blue"], colors["clean"]))
else:
    print("{}Welcome, Lady{}".format(colors["purple"], colors["clean"]))
