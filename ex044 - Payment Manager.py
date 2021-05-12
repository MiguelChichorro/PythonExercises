from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
price = float(input("Enter the product price you go to buy: "))
method = int(input("Enter 1 if you want to buy in cash or 2 to buy in card: "))
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
if method == 1:
    price = price - (price * 0.10)
    print("The price with 10% off is {}US${:.2f}{}".format(colors["green"], price, colors["clean"]))
elif method == 2:
    method = int(input("Enter 1 if want to pay cash or 2 to installment: "))
    if method == 1:
        price = price - (price * 0.05)
        print("The price with 5% off is {}US${:.2f}{}".format(colors["green"], price, colors["clean"]))
    elif method == 2:
        install = int(input("How many times do you want to pay? "))
        if install == 2:
            print("The price is {}US${:.2f}{}".format(colors["green"], price, colors["clean"]))
        else:
            price = (price + (price * 0.20) * install)
            install = install * 20
            print("The price with {}{}%{} with interest is {}US${:.2f}{}"
                  .format(colors["red"], install, colors["clean"],
                          colors["green"], price, colors["clean"]))
    else:
        print("{}You need to type 1 or 2{}".format(colors["red"], colors["clean"]))
else:
    print("{}You need to type 1 or 2{}".format(colors["red"], colors["clean"]))


