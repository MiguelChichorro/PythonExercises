colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
contw = 0
sumage = 0
old = 0
nmold = ""
for c in range(1, 5):
    print("------- {} Person -------".format(c))
    name = str(input("Enter a name: ")).strip().upper()
    gender = int(input("Enter your gender""\n {}[ 1 ] Man{} {}[ 2 ] Woman{}\n: "
                       .format(colors["blue"], colors["clean"], colors["purple"], colors["clean"])))
    age = int(input("Enter the age: "))
    sumage += age
    names = name.split()
    if gender == 2 and age < 20:
        contw += 1
    if c == 1 and gender == 1 or gender == 1 and old < age:
        old = age
        nmold = names[0]
avg = sumage / 4
print("{}The age average is {}{}".format(colors["yellow"], avg, colors["clean"]))
if old == 0:
    print("{}There are not Men{}".format(colors["red"], colors["clean"]))
else:
    print("{}the older man is {} years old and his name is {}{}".format(colors["blue"], old, nmold, colors["clean"]))
if contw > 0:
    print("{}The number of minor women is {}{}".format(colors["purble"], contw, colors["clean"]))
else:
    print("{}There are not Women{}".format(colors["red"], colors["clean"]))
