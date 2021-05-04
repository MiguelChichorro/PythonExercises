colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
some = input('Type something: ')
print('The primal type of your thing is {} '.format(type(some)))
print('It´s numeric? {}'.format(some.isnumeric()))
print('It´s alphabet? {}'.format(some.isalpha()))
print('It´s alphanumeric? {}'.format(some.isalnum()))
print('It´s all in capital letter? {}'.format(some.isupper()))
print('It´s all in lowercase? {}'.format(some.islower()))
print('It´s title? {}'.format(some.istitle()))
print('Just has spaces? {}'.format(some.isspace()))
