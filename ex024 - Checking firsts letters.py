from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
city = str(input("Enter the name about any city: ")).strip()
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
city = city.split()
print("The name of the city you Enter begin with {}Santo?{} {}{}{}"
      .format(colors["cian"], colors["clean"],
              colors["cian"], "SANTO" in city[0].upper(), colors["clean"]))
