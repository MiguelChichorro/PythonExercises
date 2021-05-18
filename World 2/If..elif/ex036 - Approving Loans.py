from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
house = float(input("Enter the house value: US$"))
pay = float(input("How many months do you want to pay? if you wanna buy in cash just Enter 0 : "))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if pay == 0:
    bank = float(input("Please Enter how much money do you have on the bank: US$"))
    if bank > house:
        print("{}Congradulations, you can buy the house{}"
              .format(colors["green"], colors["clean"]))
    else:
        print("{}Sorry but the house value is greater than the value you have in your account{}"
              .format(colors["red"], colors["clean"]))
elif pay != 0:
    salary = float(input("Enter your salary: US$"))
    monpay = house / (pay * 12)
    housal = salary * 0.30
    if monpay < housal:
        print("{}You can buy this house and the monthly payment is US${:.2f}{}"
              .format(colors["green"], monpay, colors["clean"]))
    else:
        print("{}Sorry but the monthly payment is US${:.2f}"
              "\nYou don´t have the money needed to buy this house{}"
              .format(colors["red"], monpay, colors["clean"]))
