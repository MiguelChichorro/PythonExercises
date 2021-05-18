from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
v = float(input("Enter the car speed was: "))
tic = (v - 80) * 7
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if v > 80:
    print("{}You were very fast, your speed was {} km{}".format(colors["red"], v, colors["clean"]))
    print("{}Now you need to pay {} $US because of that{}".format(colors["red"], tic, colors["clean"]))
else:
    print("{}You were in the right speed, you can move on{}".format(colors["green"], colors["clean"]))
