from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
print("{}{:=^40}{}".format(colors["cian"], " Miguelitos ", colors["clean"]))
price = float(input("Enter the product price you go to buy: US$"))
method = int(input("Enter\n[ 1 ] if you want to buy in cash\n[ 2 ] to buy in card: "))
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if method == 1:
    price = price - (price * 0.10)
    print("The price with 10% off is {}US${:.2f}{}".format(colors["green"], price, colors["clean"]))
elif method == 2:
    method = int(input("Enter\n[ 1 ] if want to pay cash\n[ 2 ] to installment: "))
    if method == 1:
        price = price - (price * 0.05)
        print("The price with 5% off is {}US${:.2f}{}".format(colors["green"], price, colors["clean"]))
    elif method == 2:
        install = int(input("How many times do you want to pay? "))
        if install == 2:
            installm = price / install
            print(
                "Your installment is {}x in card and installment US${}\nThe final price with interest is {}US${:.2f}{}"
                .format(install, installm, colors["green"], price, colors["clean"]))
        else:
            price = (price + (price * 0.20))
            installm = price / install
            print("Your installment is {}x in card and installment US${}\nThe final price with interest is {}US${:.2f}{}"
                  .format(install, installm, colors["green"], price, colors["clean"]))
    else:
        print("{}You need to type 1 or 2{}".format(colors["red"], colors["clean"]))
else:
    print("{}You need to type 1 or 2{}".format(colors["red"], colors["clean"]))
print("{}{:=^40}{}".format(colors["cian"], " Miguelitos ", colors["clean"]))
