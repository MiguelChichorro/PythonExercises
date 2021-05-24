colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    n2, n1, cont = 1, 0, 0
    nterm = int(input("Enter How many terms you want: "))
    while cont < nterm:
        print("{}{}{}".format(colors["yellow"], n1, colors["clean"]), end=" -> ")
        nte = n1 + n2
        n1 = n2
        n2 = nte
        cont += 1
    print("END", end="")
    ans = int(input("{}\nIf you want to do again\nEnter [ 1 ]\nAnother number to leave:{} ".format(colors["blue"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))
