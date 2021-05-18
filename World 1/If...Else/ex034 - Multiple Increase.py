from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
sal = int(input("Enter your salary:"))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(2)
if sal > 1250:
    newsal = sal + (sal * 0.10)
    print("{}Your new salary with 10% increase is US${}{}".format(colors["green"], newsal, colors["clean"]))
else:
    newsal = sal + (sal * 0.15)
    print("{}Your new salary with 15% increase is US${}{}".format(colors["green"], newsal, colors["clean"]))
print("{}Congratulations!!!{}".format(colors["yellow"], colors["clean"]))
