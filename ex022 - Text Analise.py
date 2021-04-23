name = str(input("Hello, please tell me your name: "))
print("your name with all letter up is {}"
      "\n and with all letters lower is {}".format(name.upper(), name.lower()))
division = name.split()
print("Your name has {} letters and your first name is {}"
      "\n nice to meet you {}".format(len(name.strip()), division[0], name))
