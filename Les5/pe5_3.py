def lijstInfo(bestand):
    inbestand = open(bestand, 'r')
    inhoud = inbestand.readlines()
    inbestand.seek(0)
    inhoudlos = inbestand.read()
    inbestand.close()

    lengtelijst = len(inhoud)                   # lengte van de lijst

    print('Deze file telt ' + str(lengtelijst) + ' regels')

    table = str.maketrans('!,.:;?', 6 * ' ')    # opschonen gegevens
    inhoudlos = inhoudlos.translate(table)
    splitinhoud = inhoudlos.split()

    nummerlijst = []                            # lijst aanmaken met allen de nummers
    for gegeven in splitinhoud:
        if gegeven.isdigit():
            nummerlijst.append(gegeven)

    maxnummer = max(nummerlijst)                # hoogste nummer uit de lijst halen

    for rij, nummers in enumerate(inhoud):      # zoeken in welke rij maxnummer zit
        if maxnummer in nummers:
            rijnummer = str(rij + 1)

    print('Het grootste kaartnummer is: ' + maxnummer + ' en dat staat op regel ' + rijnummer)


lijstInfo('kaartnummers.txt')
