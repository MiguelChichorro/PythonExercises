from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height / 100) ** 2
print("{}reading data...{}".format(colors["green"], colors["clean"]))
sleep(0.5)
print("{}Your Body Mass Index is {:.2f}{}".format(colors["cian"], bmi, colors["clean"]))
if bmi < 18.5:
    print("{}You are Underweight, be alert{}".format(colors["yellow"], colors["clean"]))
elif (bmi >= 18.5) and (bmi <= 24.9):
    print("{}You are Normal weight, keep it up{}".format(colors["green"], colors["clean"]))
elif (bmi >= 25.0) and (bmi <= 29.9):
    print("{}You are Pre-obesity, be alert{}".format(colors["yellow"], colors["clean"]))
elif (bmi >= 30.0) and (bmi <= 34.9):
    print("{}You are Obesity Class I, be careful{}".format(colors["red"], colors["clean"]))
elif (bmi >= 35.0) and (bmi <= 39.9):
    print("{}You are Obesity Class II, be careful{}".format(colors["red"], colors["clean"]))
else:
    print("{}You are Obesity Class III, be careful{}".format(colors["red"], colors["clean"]))
