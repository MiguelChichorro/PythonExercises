ph = str(input("Type any phrase here: "))
ph = ph.strip()
print("This phrase has {} letters A"
      "\n The first position is {}"
      "\n And the last is {}".format(ph.upper().count("A"), ph.upper().find("A"), ph.upper().rfind("A")))
