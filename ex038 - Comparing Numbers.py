from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if num1 > num2:
    print("{}{} is bigger than {}{}"
          .format(colors["blue"], num1, num2, colors["clean"]))
elif num2 > num1:
    print("{}{} is bigger than {}{}"
          .format(colors["yellow"], num2, num1, colors["clean"]))
else:
    print("{}The two numbers are equal{}"
          .format(colors["red"], colors["clean"]))

