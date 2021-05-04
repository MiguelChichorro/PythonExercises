colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Type how many money do you have in your wallet(in Real): R$"))
print("You have R${:.2f} reals and you can buy US${:.2f} dollars"
      "\n Buy EUR${:.2f} and buy GBP${:.2f}".format(n1, n1/5.59, n1/6.69, n1/7.79))
