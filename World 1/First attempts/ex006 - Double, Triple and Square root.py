colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input("Enter a number: "))
print("Your number is {}{}{}"
      "\nThe double of your number is {}{}{}"
      "\nThe triple is {}{}{}"
      "\nThe square root is {}{:.2f}{}"
      .format(colors["purple"], n1, colors["clean"],
              colors["purple"], n1*2, colors["clean"],
              colors["purple"], n1*3, colors["clean"],
              colors["purple"], pow(n1, 1/2), colors["clean"]))
