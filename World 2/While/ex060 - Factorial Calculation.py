colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    fac = 1
    n = int(input("Input a number to compute the factiorial : "))
    print("Calculing {}! = ".format(n), end="")
    while n > 0:
        print("{}". format(n), end="")
        print(" x " if n > 1 else " = ", end="")
        fac = fac * n
        n -= 1
    print("{}{}{}".format(colors["green"], fac, colors["clean"]), end="")
    ans = int(input("\n{}Press [ 1 ] to do again or another number to leave: {}".format(colors["cian"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))
