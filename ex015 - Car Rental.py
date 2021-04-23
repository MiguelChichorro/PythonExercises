Km = float(input("How many kms do you traveled with this car? "))
Day = int(input("How many days do you got with this car? "))
Pay = (Km * 0.15) + (Day * 60)
print("You traveled {:.1f}Kms and got {} days whit this car,"
      "\n the days costs R$60 and every Km traveled costs R$0,15, so you need to pay R${:.2f}".format(Km, Day, Pay))
