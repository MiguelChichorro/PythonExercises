colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans, termadd, ans2 = 1, 0, 0
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
    ans2 = int(input("\n{}If you want to see more terms{}\n{}Enter [ 1 ]{}\n{}Another number to leave:{} "
                     .format(colors["blue"], colors["clean"], colors["yellow"], colors["clean"], colors["red"], colors["clean"])))
    while ans2 == 1:
        cont, terms = 0, 1
        termadd = int(input("{}Enter the number of terms you want to see more:{} "
                            .format(colors["blue"], colors["clean"])))
        while cont < termadd:
            print("{}{} {}".format(colors["yellow"], term, colors["clean"]), end="-> ")
            term += r
            cont += 1
        print("END", end="")
        ans2 = int(input("{}\nPress [ 1 ] to add more terms{}\n{}Another number to leave:{} "
                         .format(colors["blue"], colors["clean"], colors["red"], colors["clean"])))
    if ans2 != 1 or termadd != 1:
        ans = int(input("{}If you want to put another term and razon{}\n{}Enter [ 1 ]{}\n{}Another number to leave:{} "
                        .format(colors["blue"], colors["clean"], colors["yellow"], colors["clean"], colors["red"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))
