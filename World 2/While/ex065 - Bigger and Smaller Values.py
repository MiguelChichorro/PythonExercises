colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    cont, avg, sum, bg, sml, again = 0, 0, 0, 0, 0, 1
    while again == 1:
        ncont = 1
        while ncont == 1:
            n = int(input("Enter a number: "))
            cont += 1
            sum = sum + n
            avg = sum / cont
            if cont == 1:
                bg = n
                sml = n
            else:
                if n > bg:
                    bg = n
                if n < sml:
                    sml = n
            ncont = int(input("{}Press [ 1 ] to enter another number{}\n{}Another number to leave:{} "
                              .format(colors["blue"], colors["clean"], colors["red"], colors["clean"])))
            if ncont != 1:
                print("{}The smaller number you enter is {}{}"
                      "\n{}The bigger number you enter is {}{}"
                      "\n{}The average between all numbers you enter is {}{}"
                      .format(colors["blue"], sml, colors["clean"],
                              colors["yellow"], bg, colors["clean"],
                              colors["purple"], avg, colors["clean"]))
                again = int(input("{}Press [ 1 ] to enter another number{}\n{}Another number to leave:{} ".format(colors["green"], colors["clean"], colors["red"], colors["clean"])))
                if again != 1:
                    ans = int(input("{}\nIf you want to do again\nEnter [ 1 ]\nAnother number to leave:{} ".format(colors["blue"], colors["clean"])))
if ans != 1:
    print("{}Have a good day!{}".format(colors["green"], colors["clean"]))