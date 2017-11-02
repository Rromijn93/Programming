import csv
# stap 1: aanmaken van CSV bestand met headers.
gegevens_schrijven = [
    {'Artikelnummer': 121, 'Artikelcode': 'ABC123', 'Naam': 'Highlight pen', 'Voorraad': 231, 'Prijs': 0.56},
    {'Artikelnummer': 123, 'Artikelcode': 'PQR678', 'Naam': 'Nietmachine', 'Voorraad': 587, 'Prijs': 9.99},
    {'Artikelnummer': 128, 'Artikelcode': 'ZYX163', 'Naam': 'Bureaulamp', 'Voorraad': 34, 'Prijs': 19.95},
    {'Artikelnummer': 137, 'Artikelcode': 'MLK709', 'Naam': 'Monitorstandaard', 'Voorraad': 66, 'Prijs': 32.50},
    {'Artikelnummer': 271, 'Artikelcode': 'TRS665', 'Naam': 'Ipad hoes', 'Voorraad': 155, 'Prijs': 19.01}]

with open("artikelen.csv", "w", newline='\n') as WriteMyCsv:
    veldnamen = ["Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"]
    writer = csv.DictWriter(WriteMyCsv, fieldnames=veldnamen, delimiter=";")
    writer.writeheader()

    for gegeven in gegevens_schrijven:
        writer.writerow(gegeven)

# stap 2: lezen van het csv bestand
with open("artikelen.csv", "r") as ReadMyCsv:
    reader = csv.DictReader(ReadMyCsv, delimiter=";")

    gegevens_lezen = []
    for row in reader:
        gegevens_lezen.append(row)

# 1. naam en prijs van het duurste product
duurste_artikel_prijs = 0
duurste_artikel_naam = None
for item in gegevens_lezen:
    prijs = float(item["Prijs"])
    if prijs == 0 or duurste_artikel_prijs < prijs:
        duurste_artikel_prijs = prijs
        duurste_artikel_naam = item["Naam"]

if duurste_artikel_prijs != 0:
    print("Het duurste artikel is {0} en die kost {1:.2f} Euro".format(duurste_artikel_naam, duurste_artikel_prijs))
else:
    print("Duurste product niet gevonden..")

# 2. artikelnummer en voorraad van het artikel met de kleinste voorraad
laagste_voorraad = 99999
laagste_artikelnr = None
for item in gegevens_lezen:
    voorraad = int(item["Voorraad"])
    if voorraad == 0 or voorraad < laagste_voorraad:
        laagste_voorraad = voorraad
        laagste_artikelnr = item["Artikelnummer"]

if laagste_voorraad != 0:
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(laagste_voorraad, laagste_artikelnr))
else:
    print("Laagste voorraad niet gevonden..")

# 3. totaal aantal producten in voorraad
voorraad_totaal = 0
for art in gegevens_lezen:
    voorraad_totaal += int(art['Voorraad'])
print("In totaal hebben wij {} producten in ons magazijn liggen".format(voorraad_totaal))