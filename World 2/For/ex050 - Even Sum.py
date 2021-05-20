colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
sumc = 0
cont = 0
for c in range(1, 7):
    print("{}----- {} Number -----{}".format(colors["cian"], c, colors["clean"]))
    sum = int(input("Enter a number: "))
    if (sum % 2) == 0:
        sumc += sum
        cont += 1
print("{}You enter {} even {} {} {}{}"
      .format(colors["blue"], cont, "numbers" if cont > 1 else "number",
              "and the sum between them is" if cont > 1 else "so don´t have a sum",
              sumc, colors["clean"]))
