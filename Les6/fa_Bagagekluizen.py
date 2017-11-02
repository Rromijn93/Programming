while True:
    print()
    print("Kies uit een van de voldende opties:")
    print()
    print("1: ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print()
    keuze_gebruiker = eval(input("Optie: "))


    def toon_aantal_kluizen_vrij():
        """Functie print het aantal kluizen dat nog beschikbaar is"""
        bestand = open('kluizen.txt', 'r')
        inhoud = bestand.readlines()
        bestand.close()

        aantal_kluizen = len(inhoud)    # kluizen in bestand
        totaal_kluizen = 12             # totaal aantal kluizen
        beschikbaar = totaal_kluizen - aantal_kluizen

        print("Kluizen beschikbaar: " + str(beschikbaar))


    def nieuwe_kluis():
        """Funtie registreert, indien beschikbaar, een nieuwe kluis met een door de gebruiker ingevoerde code"""
        kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        bestand = open('kluizen.txt', 'r')
        inhoud = bestand.readlines()
        bestand.close()

        # lezen van kluizen uit bestand
        kluizen_bezet = []
        for rij in inhoud:
            kluizen_bezet.append((rij.split(';'))[0])

        # bepalen welke kluizen nog beschikbaar zijn
        for kluis in range(1, 13):
            if str(kluis) in kluizen_bezet:
                kluizen.remove(kluis)

        # vragen om kluiscode, schrijven gegevens en teruggeven toegewezen kluisnummer.
        if len(kluizen) > 0:
            kluis_code = input("Kluiscode: ")
            toegewezen_kluis = kluizen[0]
            bestand_schrijven = open('kluizen.txt', 'a')

            bestand_schrijven.write(str(toegewezen_kluis) + ';' + kluis_code + '\n')
            bestand_schrijven.close()

            print("Je hebt kluisnummer: " + str(toegewezen_kluis))
        else:
            print("Er zijn helaas geen kluizen meer beschikbaar..")


    def kluis_openen():
        """Functie opent een kluis aan de hand van overeenkomende kluisnummer en kluiscode"""
        kluisnummer = eval(input("Wat is je kluisnummer: "))
        kluiscode = input("Wat is je kluiscode: ")

        bestand = open('kluizen.txt', 'r' )
        inhoud = bestand.read()
        bestand.close()

        # controle of invoer van gebruiker overeenkomt met bestand
        inhoud_regels = inhoud.split('\n')
        nummercode = str(kluisnummer) + ";" + kluiscode
        if len(inhoud_regels) > 1:
            kluis_open = ''
            for item in inhoud_regels:
                if item == nummercode:
                    kluis_open = True

            if kluis_open == True:
                print("Je kluis is open!")
            else:
                print("De ingevoerde gegevens kloppen niet..")
        else:
            print("Er zijn geen kluizen in gebruik..")


    def kluis_teruggeven():
        """Functie geeft een kluis vrij aan de hand van overeenkomende kluisnummer en kluiscode"""
        kluisnummer = eval(input("Wat is je kluisnummer: "))
        kluiscode = input("Wat is je kluiscode: ")

        bestand = open('kluizen.txt', 'r')
        inhoud = bestand.read()
        bestand.seek(0)
        inhoud_lines = bestand.readlines()
        bestand.close()

        inhoud_regels = inhoud.split('\n')
        nummercode = str(kluisnummer) + ";" + kluiscode
        nummercode_str = nummercode + "\n"

        # controle of invoer van gebruiker overeenkomt met bestand
        if len(inhoud_regels) > 1:
            kluis_open = ''
            for item in inhoud_regels:
                if item == nummercode:
                    kluis_open = True

        # verwijderen van vrijgegeven kluis uit bestand
            if kluis_open == True:
                bestand_aanpassen = open('kluizen.txt', 'w')
                inhoud_lines.remove(nummercode_str)
                for gegeven in inhoud_lines:
                    bestand_aanpassen.write(gegeven)
                bestand_aanpassen.close()
                print("Je kluis is vrijgegeven")
            else:
                print("De ingevoerde gegevens kloppen niet..")
        else:
            print("Er zijn geen kluizen in gebruik..")

    if keuze_gebruiker == 1:
        toon_aantal_kluizen_vrij()
    elif keuze_gebruiker == 2:
        nieuwe_kluis()
    elif keuze_gebruiker == 3:
        kluis_openen()
    elif keuze_gebruiker == 4:
        kluis_teruggeven()
    elif keuze_gebruiker == 0:
        break
    else:
        print("Er is niet gekozen voor een beschikbare optie..")