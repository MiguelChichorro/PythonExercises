colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    print(f"{colors['green']}={colors['clean']}" * 20)
    print("{}{:^30}{}".format(colors['green'], "$$$BANK$$$", colors['clean']))
    print(f"{colors['green']}={colors['clean']}" * 20)
    value = int(input("Enter the amount to withdraw: "))
    total = value
    moneybill = 100
    totalmoney = 0
    while True:
        if total >= moneybill:
            total -= moneybill
            totalmoney += 1
        else:
            if totalmoney > 0:
                print(f"{colors['green']}You need {totalmoney} {'money bill ' if totalmoney == 1 else 'money bills '}{moneybill}US${colors['green']}")
            if moneybill == 100:
                moneybill = 50
            elif moneybill == 50:
                moneybill = 20
            elif moneybill == 20:
                moneybill = 10
            elif moneybill == 10:
                moneybill = 1
            totalmoney = 0
            if total == 0:
                break
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}={colors['clean']}" * 25)
    print("{}{:^30}{}".format(colors['green'], "$$$CHECK BACK OFTEN$$$", colors['clean']))
    print(f"{colors['green']}={colors['clean']}" * 25)
