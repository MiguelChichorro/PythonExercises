colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Type a a number? "))
if num % 2 == 0:
    print("\033[33mThe number {} is a even number\033[m".format(num))
else:
    print("\033[35mThe number {} is a odd number\033[m".format(num))
