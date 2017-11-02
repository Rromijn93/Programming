def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')


lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

# Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
    # Omdat er geen return in de functie zit nee..

# Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
    # Werkt niet omdat de functie is gemaakt voor een list. en een string is "immutable".

# Welke rol speeld (im)mutabiliteit in deze vraag?
