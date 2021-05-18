colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input("Enter any number: "))
print("{}={}".format(colors["red"], colors["clean"])*12)
print("{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      "\n{} * {:2} = {}"
      .format(n1, 0, n1*0,
              n1, 1, n1*1,
              n1, 2, n1*2,
              n1, 3, n1*3,
              n1, 4, n1*4,
              n1, 5, n1*5,
              n1, 6, n1*6,
              n1, 7, n1*7,
              n1, 8, n1*8,
              n1, 9, n1*9,
              n1, 10, n1*10))
print("{}={}".format(colors["red"], colors["clean"])*12)
