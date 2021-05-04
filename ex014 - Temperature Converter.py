colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
C = float(input("Type degree Celsius:"))
F = (C * 9 / 5) + 32
K = C + 273.15
print("Your degree Celsius is {:.0f}°C, in degree Fahrenheit is {:.0f}°F and in degree Kelvin is {:.0f}°K". format(C, F, K))
