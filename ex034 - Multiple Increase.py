colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
sal = int(input("Type your salary:"))
if sal > 1250:
    newsal = sal + (sal * 0.10)
    print("\033[33mYour new salary with 10% increase is US${}\033[m".format(newsal))
else:
    newsal = sal + (sal * 0.15)
    print("\033[33mYour new salary with 15% increase is US${}\033[m".format(newsal))
print("\033[34mCongratulations!!!\033[m")