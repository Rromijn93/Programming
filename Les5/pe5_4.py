def registratie(bestand):
    bestand = open(bestand, 'a')  # aanmaken of bewerken bestand

    import datetime  # huidige datum en tijd
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%a %d %b %Y')
    tijd = vandaag.strftime('%H:%M')

    naamhardloper = input('Naam van de hardloper: ')  # naam hardloper verkijgen

    bestand.write(datum + ', ' + tijd + ', ' + naamhardloper + '\n')  # schrijven van gegevens
    bestand.close()


registratie('hardlopers.txt')
