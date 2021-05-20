colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
sumc = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        cont = cont + 1
        sumc = sumc + c
print("|| {}The total numbers is {} And the sum between them is {:3}{} ||".format(colors["yellow"], cont, sumc, colors["clean"]))
