colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Type your name please: ")).strip()
print("Nice to meet you {}".format(name))
name = name.split()
print("First name {}"
      "\nLast name {}".format(name[0], name[-1]))
