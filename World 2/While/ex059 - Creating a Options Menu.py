colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    ch = 4
    n1 = 0
    n2 = 0
    while ch == 4:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))
        ch = int(input("Enter the numbers\n{}[ 1 ] SUM{}\n{}[ 2 ] MULTIPLY{}\n{}[ 3 ] BIGGER{}\n{}[ 4 ] NEW NUMBERS{}\n{}[ 5 ] TO LEAVE{}\n:"))
    if ch == 1:
        sum = n1 + n2
        print("{}The sum between {} and {} is {}{}")
    elif ch == 2:
        mult = n1 * n2
        print("{}The multiplication between {} and {} is {}{}")
    elif ch == 3:
        if n1 > n2:
            print("{}{} is bigger than {}{}"
                  .format(colors["blue"], n1, n2, colors["clean"]))
        elif n2 > n1:
            print("{}{} is bigger than {}{}"
                  .format(colors["yellow"], n2, n1, colors["clean"]))
        else:
            print("{}The two numbers are equal{}"
                  .format(colors["red"], colors["clean"]))
    if ch != 5:
        ans = int(input("{}Press [ 1 ] to do again or another number to leave{}"))
if ch == 5 or ans != 1:
    print("{}Have a good day!{}")
