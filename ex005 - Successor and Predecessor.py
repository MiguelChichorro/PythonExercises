colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input("Type a number: "))
print("Your number is {}, the successor of your number is {} and the predecessor is {}".format(n1, n1+1, n1-1))
