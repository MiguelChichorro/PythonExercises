colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
some = input('Enter something: ')
print('{}The primal Enter of your thing is {}{} '.format(colors["blue"], type(some), colors["clean"]))
print('{}It´s numeric? {}{}'.format(colors["green"], some.isnumeric(), colors["clean"]))
print('{}It´s alphabet? {}{}'.format(colors["red"], some.isalpha(), colors["clean"]))
print('{}It´s alphanumeric? {}{}'.format(colors["cian"], some.isalnum(), colors["clean"]))
print('{}It´s all in capital letter? {}{}'.format(colors["purple"], some.isupper(), colors["clean"]))
print('{}It´s all in lowercase? {}{}'.format(colors["yellow"], some.islower(), colors["clean"]))
print('{}It´s title? {}{}'.format(colors["red"], some.istitle(), colors["clean"]))
print('{}Just has spaces? {}{}'.format(colors["cian"], some.isspace(), colors["clean"]))
