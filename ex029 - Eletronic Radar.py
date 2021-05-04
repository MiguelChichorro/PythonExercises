colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
v = float(input("type the car speed was: "))
tic = (v - 80) * 7
if v > 80:
    print("\033[31mYou were very fast, your speed was {} km\033[m".format(v))
    print("\033[31mNow you need to pay {} $US because of that\033[m".format(tic))
else:
    print("\033[32mYou were in the right speed, you can move on\033[m")
