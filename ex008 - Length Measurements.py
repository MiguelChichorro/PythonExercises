n1 = float(input("Type some number in meters: "))
print("Your number in meters is {:.0f}"
      " \n in km is {} km "
      "\n in hm is {} hm"
      "\n in dam is {} dam"
      "\n in dm is {:.0f} dm"
      "\n in cm is {:.0f} cm"
      "\n in mm is {:.0f} mm".format(n1, n1/1000, n1/100, n1/10, n1*10, n1*100, n1*1000))
