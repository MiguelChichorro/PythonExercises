colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = input('Type your name: ')
print('{}Nice to meet you, {}{}{}'.format(colors["blue"], colors["clean"], colors["yellow"], name))
