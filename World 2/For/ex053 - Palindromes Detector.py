colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ph = str(input("Enter any phrase: ")).strip().upper()
print("{}You enter with the phrase {}{}".format(colors["cian"], ph, colors["clean"]))
words = ph.split()
togt = "".join(words)
inv = togt[::-1]
print("{}The reverse is {}{}".format(colors["yellow"], inv, colors["clean"]))
if inv == togt:
    print("{}{} is a palindrome{}".format(colors["green"], ph, colors["clean"]))
else:
    print("{}{} is not a palindrome{}".format(colors["red"], ph, colors["clean"]))
