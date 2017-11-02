import csv

bestand = "gameinformatie.csv"

# lezen gegevens is CSV bestand
with open(bestand, 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    gegevens = []
    for row in reader:
        gegevens.append(row)

    # bepalen hoogste score bestand
    scores = []
    for score in gegevens:
        scores.append(score[2])
    scores.sort()
    hoogste_score = scores[-1]

    # printen van gegevens gamer met de hoogste score
    for item in gegevens:
        if hoogste_score in item:
            print("De hoogste score is: " + item[2] + " op " + item[1] + " behaald door " + item[0])

