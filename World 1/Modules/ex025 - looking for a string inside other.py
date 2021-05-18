from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
name = str(input("Enter your name: "))
print("{}Hmm...let me see{}".format(colors["cian"], colors["clean"]))
sleep(2)
name = name.strip()
print("Your name is {}{}{} and your name has the word Silva? {}"
      .format(colors["cian"], name, colors["clean"],
              colors["cian"], "SILVA" in name.upper(), colors["clean"]))
