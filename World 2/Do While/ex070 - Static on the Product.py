colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    cheapname = ""
    contprice = contproduct = cheaprice = sum = 0
    while True:
        price = ans2 = 0
        name = ""
        print("=" * 20)
        name = str(input("Enter the product name: "))
        while name == "":
            name = str(input(f"{colors['red']}Enter a valid product name: {colors['clean']}"))
        price = int(input("Enter the product price: "))
        sum += price
        contproduct += 1
        if price > 1000:
            contprice += 1
        if contproduct == 1:
            cheaprice = price
            cheapname = name
        elif price < cheaprice:
            cheaprice = price
            cheapname = name
        ans2 = int(input(f"{colors['green']}\nPress [ 1 ] to enter another product or another number to leave: {colors['clean']}"))
        if ans2 != 1:
            break
    if contproduct == 1:
        print(f"{colors['yellow']}You just enter one product so the total price is {sum}US${colors['clean']}")
        if contprice == 1:
            print(f"{colors['yellow']}You just enter one product and the price is over 1000US${colors['clean']}")
        else:
            print(f"{colors['yellow']}You just enter one product and the price is not over 1000US${colors['clean']}")
    else:
        print(f"{colors['yellow']}You enter {contproduct} products and the total price is {sum}US${colors['clean']}")
        if contprice == 1:
            print(f"{colors['yellow']}You enter {contproduct} products but just one has the price over 1000US${colors['clean']}")
        elif contprice == 0:
            print(f"{colors['yellow']}You enter {contproduct} products and any product has the price over 1000US${colors['clean']}")
        else:
            print(f"{colors['yellow']}You enter {contproduct} products and {contprice} has the price over 1000US${colors['clean']}")
        print(f"{colors['yellow']}The produt more cheap is {cheapname} and the price is {cheaprice}US${colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
