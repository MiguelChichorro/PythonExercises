colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
print("=" * 22)
print("{}10 AP TERMS USING WHILE{}".format(colors["cian"], colors["clean"]))
print("=" * 22)
while ans == 1:
    cont = 0
    term = int(input("Enter the first term: "))
    r = int(input("Enter the razon: "))
    while cont < 10:
        print("{}{} {}".format(colors["yellow"], term, colors["clean"]), end="-> ")
        term += r
        cont += 1
    print("End")
    ans = int(input("{}\nPress [ 1 ] to do again or another number to leave: {}".format(colors["cian"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))