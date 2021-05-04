colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ph = str(input("Type any phrase here: ")).upper().strip()
print("This phrase has {} letters A"
      "\n The first position is {}"
      "\n And the last is {}".format(ph.count("A"), ph.find("A")+1, ph.rfind("A")+1))
