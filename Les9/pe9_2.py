# programma voor het vastleggen van personen in een overheidssysteem
import datetime
import csv

bestand = 'inloggers.csv'

# schrijven van het CSV bestand
with open(bestand, "w", newline='') as WriteMyCsv:
    veldnamen = ("datumtijd", "naam", "voorl", "gbdatum", "email")
    writer = csv.writer(WriteMyCsv, delimiter=";")
    writer.writerow(veldnamen)

    while True:
        # verkrijgen van datum en tijd
        vandaag = datetime.datetime.today()
        datum_tijd = vandaag.strftime('%a %d %b %Y at %H:%M')

        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        # schrijven de gegevens in het CSV bestand
        writer.writerow((datum_tijd, voorl, naam, gbdatum, email))
