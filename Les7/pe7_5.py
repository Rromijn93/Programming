def namen():
    namen_lijst = []
    counter = {}
    naam = input("Geef een naam: ")
    namen_lijst.append(naam)

    while True:
        naam = input("Volgende naam: ")

        if naam == '':
            break

        namen_lijst.append(naam)

    for item in namen_lijst:

        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    for key, value in counter.items():
        if value == 1:
            print("Er is " + str(value) + " student met de naam " + key)
        else:
            print("Er zijn " + str(value) + " studenten met de naam " + key)


namen()
