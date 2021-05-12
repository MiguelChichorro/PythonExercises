colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
sum = n1 + n2
print('Your first number was {}{}{} '
      '\nAnd your second was {}{}{} '
      '\nThe sum between them is {}{}{}'
      .format(colors["blue"], n1, colors["clean"],
              colors["red"], n2, colors["clean"],
              colors["green"], sum, colors["clean"]))
