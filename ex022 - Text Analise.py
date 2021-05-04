colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Hello, please tell me your name: ")).strip()
print("your name with all letter up is {}"
      "\n and with all letters lower is {}".format(name.upper(), name.lower()))
division = name.split()
print("Your name has {} letters and your first name is {} and has {} letters"
      "\n Nice to meet you {}".format(len(name) - name.count(" "), division[0], len(division[0]), name))
