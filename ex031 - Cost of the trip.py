from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
trip = int(input("Type your travel distance in km: "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if trip > 200:
    price = trip * 0.45
    print("{}The travel cost is US${}{}".format(colors["cian"], price, colors["clean"]))
else:
    price = trip * 0.50
    print("{}The travel cost is US${}{}".format(colors["cian"], price, colors["clean"]))