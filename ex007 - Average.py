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
print("The average you got on the two months is {:.1f}".format((n1 + n2 + n3)/3))
