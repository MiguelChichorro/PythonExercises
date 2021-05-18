from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = int(input("Enter a number: "))
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
for c in range(0, 11):
    result = c * num
    print("{}| {} * {} = {:3} |{}".format(colors["cian"], c, num, result, colors["clean"]))
