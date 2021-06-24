colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    expression = list()
    expre = str(input("Enter a Matematic Expression: "))
    for simb in expre:
        if simb == "(":
            expression.append("(")
        elif simb == ")":
            if len(expression) > 0:
                expression.pop()
            else:
                expression.append(")")
                break
    if len(expression) == 0:
        print(f"{colors['green']}Your expression is ok {colors['clean']}")
    else:
        print(f"{colors['red']}Your expression is wrong {colors['clean']}")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")