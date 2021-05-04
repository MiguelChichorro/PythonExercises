colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
lin1 = float(input("Type the first length: "))
lin2 = float(input("Type the second length: "))
lin3 = float(input("Type the Third length: "))
if (lin1 + lin2) > lin3 and (lin1 + lin3) > lin2 and (lin2 + lin3) > lin1:
    print("\033[32mYou can make a triangle with these lengths"
          "\nBecause the sum between {} and {} is bigger than {}\033[m".format(lin1, lin2, lin3))
else:
    print("\033[31mYou can´t make a triangle with these lengths"
          "\nBecause the sum between {} and {} isn´t bigger than {}\033[m".format(lin1, lin2, lin3))
