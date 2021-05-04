colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
number = int(input("Type any number int between 0 and 9999: "))
u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
th = number // 1000 % 10
print("Unity: {}"
      "\nTens: {}"
      "\nHundreds: {}"
      "\nThousand: {}".format(u, t, h, th))
