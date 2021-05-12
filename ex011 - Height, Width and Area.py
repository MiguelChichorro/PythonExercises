colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = float(input("Enter in meters the height of your wall: "))
n2 = float(input("Enter in meters the the width of your wall: "))
area = n1 * n2
paint = area / 2
print("Your wall are is {}{}{}m²"
      "\nand you need {}{}{} liters of paint for paint all the wall"
      .format(colors["blue"], area, colors["clean"],
              colors["yellow"], paint, colors["clean"]))
