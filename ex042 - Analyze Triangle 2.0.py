from time import sleep
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
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if (lin1 + lin2) > lin3 and (lin1 + lin3) > lin2 and (lin2 + lin3) > lin1:
    print("{}You can make a triangle with these lengths"
          "\nBecause the sum between {} and {} is bigger than {}{}".format(colors["green"], lin1, lin2, lin3, colors["clean"]))
    if lin1 == lin2 and lin2 == lin3:
        print("{}Your triangle is a equilateral{}".format(colors["yellow"], colors["clean"]))
    elif lin1 == lin2 or lin1 == lin3 or lin3 == lin2:
        print("{}Your triangle is a isosceles{}".format(colors["yellow"], colors["clean"]))
    else:
        print("{}Your triangle is a scalene{}".format(colors["yellow"], colors["clean"]))
else:
    print("{}You can´t make a triangle with these lengths"
          "\nBecause the sum between {} and {} isn´t bigger than {}{}".format(colors["red"], lin1, lin2, lin3, colors["clean"]))
