colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
h = 0
l = 0
for c in range(1, 6):
    kg = float(input("Enter a weight in kg: "))
    if c == 1:
        h = kg
        l = kg
    else:
        if kg > h:
            h = kg
        if kg < l:
            l = kg
print("{}The smaller weight is {} and the bigger is {}{}".format(colors["cian"], l, h, colors["clean"]))
