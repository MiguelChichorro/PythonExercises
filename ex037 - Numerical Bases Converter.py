from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Enter a number: "))
print("{} [ 1 ] If you want to convert to Binary{}"
      .format(colors["cian"], colors["clean"]))
print("{} [ 2 ] If you want to convert to Octal{}"
      .format(colors["yellow"], colors["clean"]))
print("{} [ 3 ] If you want to convert to Hexadecimal{}"
      .format(colors["purple"], colors["clean"]))
deci = int(input("Enter here: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if deci == 1:
    print("{}Your number is {}"
          "\nConverting in Binary is {}{}"
          .format(colors["cian"], num, bin(num)[2:], colors["clean"]))
elif deci == 2:
    print("{}Your number is {}"
          "\nConveting in Octal is {}{}"
          .format(colors["yellow"], num, oct(num)[2:], colors["clean"]))
elif deci == 3:
    print("{}Your number is {}"
          "\nConverting in Hexadecimal is {}"
          .format(colors["purple"], num, hex(num)[2:], colors["clean"]))
else:
    print("{}Please Enter the numbers 1, 2 and 3 only{}"
          .format(colors["red"], colors["clean"]))
