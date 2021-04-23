from math import hypot
ca = float(input("Type the value of the adjacent over: "))
co = float(input("Type the value of the opposite over: "))
'''hyp = (pow(ca, 2) + pow(co, 2)) ** (1/2)'''
hyp = hypot(co, ca)
print(" The adjacent over is {:.2f} and the opposite over is {:.2f} \n Doing the count we have {:.2f} like Hypotenuse".format(ca, co, hyp))
