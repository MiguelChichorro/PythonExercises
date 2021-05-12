from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Enter a number: "))
print("{}If you want to convert to binary Enter 1{}"
      .format(colors["cian"], colors["clean"]))
print("{}If you want to convert to octal Enter 2{}"
      .format(colors["yellow"], colors["clean"]))
print("{}If you want to convert to Hexadecimal Enter 3{}"
      .format(colors["purple"], colors["clean"]))
deci = int(input("Enter here: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if deci == 1:
    bina = bin(num)
    print("{}Your number is {}"
          "\nConverting in Binary is {}{}"
          .format(colors["cian"], num, bina, colors["clean"]))
elif deci == 2:
    octa = oct(num)
    print("{}Your number is {}"
          "\nConveting in Octal is {}{}"
          .format(colors["yellow"], num, octa, colors["clean"]))
elif deci == 3:
    hexa = hex(num)
    print("{}Your number is {}"
          "\nConverting in Hexadecimal is {}"
          .format(colors["purple"], num, hexa, colors["clean"]))
else:
    print("{}Please Enter the numbers 1, 2 and 3 only{}"
          .format(colors["blue"], colors["clean"]))
