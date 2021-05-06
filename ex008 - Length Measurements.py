colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Type some number in meters: "))
print("{}Your number in meters is {:.0f} m"
      "\nIn km is {} km "
      "\nIn hm is {} hm"
      "\nIn dam is {} dam"
      "\nIn dm is {:.0f} dm"
      "\nIn cm is {:.0f} cm"
      "\nIn mm is {:.0f} mm{}"
      .format(colors["yellow"], n1, n1/1000, n1/100, n1/10, n1*10, n1*100, n1*1000, colors["clean"]))
