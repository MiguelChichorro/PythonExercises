from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Enter a a number? "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if num % 2 == 0:
    print("{}The number {} is a even number{}".format(colors["yellow"], num, colors["clean"]))
else:
    print("{}The number {} is a odd number{}".format(colors["purple"], num, colors["clean"]))
