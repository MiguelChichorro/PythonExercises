colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def area(b, h):
    a = b * h
    print(f"{colors['blue']}The base is {b}, The height is {h} and the area is {a}{colors['clean']}")


print("Ground Control")
print("-" * 29)
area(b=float(input("Enter the Base (m):")), h=float(input("Enter the Height (m): ")))
