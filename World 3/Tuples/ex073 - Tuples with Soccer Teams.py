colors = {"clean": "\033[m",
          "red": "\033[31m",
          "green": "\033[32m",
          "yellow": "\033[33m",
          "blue": "\033[34m",
          "purple": "\033[35m",
          "cian": "\033[36m"}
teams = ("0", "Fortaleza", "Athletico-PR", "Atlético-GO", "Bragantino", "Bahia", "Fluminense", "Palmeiras", "Flamengo",
         "Atlético-MG",
         "Corinthians", "Ceará", "Santos", "Cuiabá", "Sport", "São Paulo", "Juventude", "Inter", "Grêmio", "América-MG",
         "Chapecoense")
print(f"{colors['green']}The teams are: {colors['clean']}")
for c in sorted(teams[1:]):
    print(f"{c}")

print(f"{colors['yellow']}The 5 first placed are")
for c in teams[1:6]:
    print(f"{c}", end=" - ")

print(f"{colors['blue']}\n\nThe 4 last placed are")
for c in teams[-4:]:
    print(f"{c}", end=" - ")

print(f"\n\n{colors['red']}The Chapecoense team is in {teams.index('Chapecoense')} place{colors['clean']}")
