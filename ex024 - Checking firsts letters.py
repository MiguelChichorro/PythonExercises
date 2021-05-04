colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
city = str(input("Type the name about any city: ")).strip()
city = city.split()
print("The name of the city you type begin with Santo? {}".format("SANTO" in city[0].upper()))
