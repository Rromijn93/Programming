def splitKaart(bestand):
    bestand = open(bestand, 'r')
    inhoud = bestand.readlines()
    bestand.close()

    nieuwelijst = []
    for kaart in inhoud:
        nieuwelijst.append(kaart.split(', ')) #split de rijen in naam en nummer

    nieuwelijst=[[item.replace('\n', '') for item in lst] for lst in nieuwelijst]

    format_kaart = '{1:} heeft het kaartnummer: {0:}'
    for kaart in nieuwelijst:
        print(format_kaart.format(kaart[0], kaart[1]))

splitKaart('kaartnummers.txt')

#oud

#def splitKaart(bestand):
#    bestand = open(bestand, 'r')
#    inhoud = bestand.read()
#    bestand.close()
#
#    kaartlijst = inhoud.split('\n') #split de lijst in rijen (kan ook nog met bestand.readlines)
#    nieuwelijst = []
#    for kaart in kaartlijst:
#        nieuwelijst.append(kaart.split(', ')) #split de rijen in naam en nummer
#    return nieuwelijst
#
#
#def maakKaart(nieuwelijst):
#    format_kaart = '{1:} heeft het kaartnummer: {0:}'
#    for kaart in nieuwelijst:
#        print(format_kaart.format(kaart[0], kaart[1]))
#
#
#maakKaart(splitKaart('kaartnummers.txt'))
