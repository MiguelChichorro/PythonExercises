colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
print("=" * 11)
print("{}10 AP TERMS{}".format(colors["yellow"], colors["clean"]))
print("=" * 11)
term = int(input("Enter the first term: "))
r = int(input("Enter the razon: "))
for c in range(1, 11):
    print("{}{} {}".format(colors["cian"], term, colors["clean"]), end="-> ")
    term += r
print("End")
