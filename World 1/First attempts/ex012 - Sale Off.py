colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Enter the product price: R$"))
sale = n1 - (n1*0.05)
print("The price with 5% off is {}R${:.2f}{}"
      .format(colors["green"], sale, colors["clean"]))
