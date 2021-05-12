from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Type the first grade: "))
n2 = float(input("Type the second grade: "))
n3 = float(input("Type the thirty grade: "))
avg = (n1 + n2 + n3) / 3
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
print("{}Your average is {:.2f}{}".format(colors["cian"], avg, colors["clean"]))
if avg < 5:
    print("{}Sorry but you don´t pass, try again next year{}".format(colors["red"], colors["clean"]))
elif (avg >= 5) and (avg <= 6.9):
    print("{}You need to do a recovery test{}".format(colors["yellow"], colors["clean"]))
else:
    print("{}Congradulations you pass!!!{}".format(colors["green"], colors["clean"]))
    if avg == 10:
        print("{}You are very smart keep it up{}".format(colors["green"], colors["clean"]))
