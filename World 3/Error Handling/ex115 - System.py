from utilities import System
from utilities.System import file
from utilities import database
from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}

arq = 'people.txt'

if not file.arquiveexist(arq):
    file.createar(arq)

while True:
    ans = System.menu(["See Refistered People", "Register Person", "Out System"])
    if ans == 1:
        sleep(1)
        # option list content
        file.readarq(arq)
    elif ans == 2:
        sleep(1)
        System.header("New Register")
        name = str(input("Enter the name: "))
        age = database.lenIn("Age: ")
        file.register(arq, name, age)
    elif ans == 3:
        sleep(0.5)
        System.header("Outing...Hope see you again later")
        sleep(2)
        break
    else:
        print(f"{colors['red']}Error dosen´t exist{colors['clean']}")
    sleep(2)
