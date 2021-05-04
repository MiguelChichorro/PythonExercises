colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
trip = int(input("Type your travel distance in km: "))
if trip > 200:
    price = trip * 0.45
    print("\033[36mThe travel cost is US${}\033[m".format(price))
else:
    price = trip * 0.50
    print("\033[36mThe travel cost is US${}\033[m".format(price))