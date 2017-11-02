cijfers_cursus = {'Marie de Boer ': 7,
                  'Hugo de Groot': 10,
                  'Daan Burger': 6,
                  'Rianne Vries': 9,
                  'Morgan Hoog': 5.8,
                  "Freek for Loop": 9.1,
                  "Peter Python": 7,
                  "Bas Basic": 6.4}

print("Studenten met een cijfer boven een 9.0:")

for key, value in cijfers_cursus.items():
    if value > 9:
        print("Naam: " + key + " " + str(value))
