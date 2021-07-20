from utilities import System
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def arquiveexist(name):
    try:
        a = open(name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createar(name):
    try:
        a = open(name, "wt+")
        a.close()
    except:
        print(f"{colors['red']}Error create arquive{colors['clean']}")
    else:
        print(f"{colors['green']}file {name} created{colors['clean']}")


def readarq(name):
    try:
        a = open(name, "rt")
    except:
        print(f"{colors['red']}Error read file{colors['clean']}")
    else:
        System.header("Registered People")
        for line in a:
            dado = line.split(";")
            dado[1] = dado[1].replace("\n", " ")
            print(f"{dado[0]:<60} {dado[1]:>3} years")
    finally:
        a.close()


def register(arq, name="<unknown>", age=0):
    try:
        a = open(arq, "at")
    except:
        print(f"{colors['red']}Error Open File{colors['clean']}")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print(f"{colors['red']}Error Register person{colors['clean']}")
        else:
            print(f"{colors['green']}New Register {name} Add{colors['clean']}")