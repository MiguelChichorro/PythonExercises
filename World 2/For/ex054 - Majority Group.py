colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
old = 0
new = 0
for c in range(1, 8):
    major = int(input("Enter seven ages: "))
    if major >= 21:
        old += 1
    else:
        new += 1
print("{}In the ages you enter {} {} minor and {} {} older{}"
      .format(colors["purple"],
              new, "person is" if new == 1 else "people are",
              old, "person is" if old == 1 else "people are",
              colors["clean"]))
