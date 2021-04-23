city = str(input("Type the name about any city: "))
city = city.split()
print("The name of the city you type begin with Santo? {}".format("SANTO" in city[0].upper()))
