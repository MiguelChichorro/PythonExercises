colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans, sum, n, cont = 1, 0, 0, 0
print("{}You can enter a lot of number\nWhen you enter 999 the sum stop\nAnd Show the sum between all numbers you enter{}"
      .format(colors["blue"], colors["clean"]))
while ans == 1:
    while n != 999:
        n = int(input("Enter a number: "))
        sum = n + sum
        cont += 1
    if cont == 0:
        print("{}You don´t enter any number to do the sum{}".format(colors["red"], colors["clean"]))
    else:
        print("{}You enter {} numbers and the sum between them is {}{}".format(colors["blue"], cont, sum, colors["clean"]))
    ans = int(input("{}\nIf you want to do again\nEnter [ 1 ]\nAnother number to leave:{} ".format(colors["blue"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))
