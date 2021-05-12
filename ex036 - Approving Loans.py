from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
house = float(input("Type the house value: "))
pay = float(input("How many months do you want to pay? if you wanna buy in cash just type 0 :"))
print("{}Loading...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if pay == 0:
    bank = float(input("Please type how much money do you have on the bank: "))
    if bank > house:
        print("{}Congradulations, you can buy the house{}"
              .format(colors["green"], colors["clean"]))
    else:
        print("{}Sorry but the house value is greater than value you have in your account{}"
              .format(colors["red"], colors["clean"]))
elif pay != 0:
    salary = float(input("Type your salary: "))
    monpay = house / pay
    housal = salary * 0.30
    if monpay < housal:
        print("{}You can buy this house and the monthly payment is {}{}"
              .format(colors["green"], monpay, colors["clean"]))
    else:
        print("{}Sorry but the monthly payment is {} and you don´t have the money needed to buy this house{}"
              .format(colors["red"], monpay, colors["clean"]))
