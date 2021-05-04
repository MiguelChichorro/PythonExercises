colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
n1 = int(input("Type the first number: "))
n2 = int(input("Type the second number: "))
n3 = int(input("Type the third number:  "))
# Who is largest
if (n1 > n2) and (n1 > n3):
    largest = n1
elif (n2 > n1) and (n2 > n3):
    largest = n2
else:
    largest = n3
# Who is smaller
if (n1 < n2) and (n1 < n2):
    smaller = n1
elif (n2 < n1) and (n2 < n1):
    smaller = n2
else:
    smaller = n2
print("The largest number is \033[36m{}\033[m and the smaller is \033[36m{}\033[m".format(largest, smaller))
