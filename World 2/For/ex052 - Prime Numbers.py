colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Enter a number: "))
cont = 0
for c in range(1, num + 1):
    if (num % c) == 0:
        cont += 1
        print("{}".format(colors["green"]), end=" ")
    else:
        print("{}".format(colors["red"]), end=" ")
    print("{}".format(c), end=" ")

print("\n{}The number {} can be divided {} times{}".format(colors["yellow"], num, cont, colors["clean"]))
if cont == 2:
    print("{}Your number is prime{}".format(colors["green"], colors["clean"]))
else:
    print("{}Your number is not prime{}".format(colors["red"], colors["clean"]))
