colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
ans = 1
while ans == 1:
    tuple = ()
    ans2 = 1
    while ans2 == 1:
        word = str(input("Enter any word: ")).upper()
        tuple += word,
        ans2 = int(input(f"{colors['green']}\nPress [ 1 ] to enter another word or another number to leave: {colors['clean']}"))
    for i in tuple:
        print(f"\nIn the word {i} we have ", end="")
        for letter in i:
            if letter.lower() in "aeiou":
                print(letter, end=" ")
    ans = int(input(f"{colors['cian']}\nPress [ 1 ] to do again or another number to leave: {colors['clean']}"))
if ans != 1:
    print(f"{colors['green']}Have a good day!{colors['clean']}")
