colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
Km = float(input("How many kms do you traveled with this car? "))
Day = int(input("How many days do you got with this car? "))
Pay = (Km * 0.15) + (Day * 60)
print("{}You traveled {:.1f}Kms and got {} days whit this car"
      "\nThe days costs R$60 and every Km traveled costs R$0,15{}"
      "\n{}You need to pay R${:.2f}{}"
      .format(colors["yellow"], Km, Day, colors["clean"],
              colors["red"], Pay, colors["clean"]))
