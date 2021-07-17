from time import sleep
colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}


def grades(num, sit=False):
    print(f"{colors['purple']}Reading data...{colors['clean']}")
    sleep(1)
    r = dict()
    r['Total'] = len(num)
    r['Bigger'] = max(num)
    r['Smaller'] = min(num)
    r['Avg'] = round(sum(num) / len(num))
    if sit:
        if r['Avg'] >= 7:
            r['Situation'] = f"{colors['green']}Good{colors['clean']}"
        elif r['Avg'] >= 5:
            r['Situation'] = f"{colors['yellow']}Reasonable{colors['clean']}"
        else:
            r['Situation'] = f"{colors['red']}Bad{colors['clean']}"
    for c, v in r.items():
        print(f"{c}: {v:}", end=" ")


ans = 1
while ans == 1:
    mark = list()
    cont = 1
    while True:
        mark.append(float(input(f"Enter the mark of the {cont}º student: ")))
        ans2 = str(input(f"Do you want do add another person? [{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]
        cont += 1
        while ans2 != "Y" and ans2 != "N":
            ans2 = str(input(f"{colors['red']}Please just enter Yes or No {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]
        if ans2 == "N":
            break
    ans3 = str(input(f"{colors['blue']}Do you want to se the class situation? {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]
    while ans3 != "Y" and ans2 != "N":
        ans3 = str(input(f"{colors['red']}Please just enter Yes or No {colors['clean']}[{colors['green']}Y{colors['clean']}/{colors['red']}N{colors['clean']}]: ")).strip().upper()[0]
    if ans3 == "Y":
        grades(mark, sit=True)
    elif ans3 == "N":
        grades(mark, sit=False)
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['cian']}Have a good day!{colors['clean']}")
