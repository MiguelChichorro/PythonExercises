colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    tuple = ()
    ans2 = 1
    while ans2 == 1:
        produ = str(input("Enter the product name: "))
        tuple += produ,
        price = int(input("Enter the product price: "))
        tuple += price,
        ans2 = int(input(f"{colors['green']}\nPress [ 1 ] to enter another product or another number to leave: {colors['clean']}"))
    print(f"{colors['cian']}={colors['clean']}" * 30)
    print(f"{colors['cian']}{'Buy List': ^50}{colors['clean']}")
    print(f"{colors['cian']}={colors['clean']}" * 30)
    for i in tuple:
        if type(i) is str:
            print(f'{i:.<32}', end='')
        else:
            print(f'US$ {i:>5.2f}')
    print(f"{colors['cian']}={colors['clean']}" * 30)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
