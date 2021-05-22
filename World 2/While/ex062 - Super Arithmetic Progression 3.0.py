colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans2 = 0
termadd = 0
ans = 1
print("=" * 22)
print("{}Super Arithmetic Progession{}".format(colors["cian"], colors["clean"]))
print("=" * 22)
while ans == 1:
    cont = 0
    term = int(input("Enter the first term: "))
    r = int(input("Enter the razon: "))
    while cont < 10:
        print("{}{} {}".format(colors["yellow"], term, colors["clean"]), end="-> ")
        term += r
        cont += 1
    print("END", end="")
    ans2 = int(input("\nIf you want to see more terms Enter [ 1 ]\n To Leave Enter [ 0 ]: "))
    while ans2 == 1:
        cont = 0
        terms = 1
        termadd = int(input("Enter the number of terms you want to see more\nEnter [ 0 ] to leave: "))
        while cont < termadd:
            print("{}{} {}".format(colors["yellow"], term, colors["clean"]), end="-> ")
            term += r
            cont += 1
        print("END", end="")
        ans2 = int(input("{}\nPress [ 1 ] to add more terms or number [ 0 ] to leave: {}".format(colors["cian"], colors["clean"])))
    if ans2 == 0 or termadd == 0:
        ans = int(input("If you want to put another term and razon enter [ 1 ]\nTo leave [ 0 ]:"))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))