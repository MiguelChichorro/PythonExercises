from ultilities import coin, database
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n = database.lenCoin("Enter How much money do you want to converse: R$")
coin.resum(n, 19, 28, True)
