from math import trunc
n1 = float(input("Type a real number: "))
print("Your number is {:.2f} and using the function trunc is {} \nBut we can use the function int to {}".format(n1, trunc(n1), int(n1)))
