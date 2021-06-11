colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
num = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
       "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
ans = 1
while ans == 1:
    usunum, cont = -1, 0
    while (usunum < 0) or (usunum > 20):
        cont += 1
        if cont == 1:
            usunum = int(input("Enter a number between 0 and 20: "))
        else:
            usunum = int(input(f"{colors['red']}Enter a number between 0 and 20: {colors['clean']}"))
    print(f"{colors['blue']}You enter the number {num[usunum]}{colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
