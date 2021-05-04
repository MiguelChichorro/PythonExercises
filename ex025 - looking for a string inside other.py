colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Type your name: "))
name = name.strip()
print("Your name is {} and your name has the word Silva? {}".format(name, "SILVA" in name.upper()))
