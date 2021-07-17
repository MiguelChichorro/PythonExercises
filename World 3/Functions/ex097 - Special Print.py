colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def write(txt):
    tam = len(txt) + 3
    print("=" * tam)
    print(f"{colors['blue']}   {txt}{colors['clean']}")
    print("=" * tam)


write(txt=str(input("Write anything: ")))
