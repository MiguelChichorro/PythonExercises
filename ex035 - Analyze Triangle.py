from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
lin1 = float(input("Enter the first length: "))
lin2 = float(input("Enter the second length: "))
lin3 = float(input("Enter the Third length: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if (lin1 + lin2) > lin3 and (lin1 + lin3) > lin2 and (lin2 + lin3) > lin1:
    print("{}You can make a triangle with these lengths"
          "\nBecause the sum between {} and {} is bigger than {}{}".format(colors["green"], lin1, lin2, lin3, colors["clean"]))
else:
    print("{}You can´t make a triangle with these lengths"
          "\nBecause the sum between {} and {} isn´t bigger than {}{}".format(colors["red"], lin1, lin2, lin3, colors["clean"]))
