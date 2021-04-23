number = str(input("Type any number int between 0 and 9999: "))
number = number.strip()
print("Unity: {}"
      "\nTens: {}"
      "\nHundreds: {}"
      "\nThousand: {}".format(number[3], number[2], number[1], number[0]))
