def inlezen_beginstation(stations):
    """Functie vraagt de gebruiker om het beginstation en geeft deze als return"""
    beginstation = input("Wat is je beginstation? : ")

    while beginstation not in stations:
        print("Geen correcte invoer.. Probeer opnieuw")

    return beginstation


def inlezen_eindstation(stations, beginstation):
    """Functie vraagt de gebruiker om het eindstation en geeft deze als retun"""
    eindstation = input("Wat is je eindstation? : ")

    while eindstation not in stations:
        print("Deze trein komt niet in " + eindstation)
        eindstation = input("Wat is je eindstation? : ")

    while stations.index(beginstation) > stations.index(eindstation):
        print("Geen correcte invoer.. Probeer opnieuw..")
        eindstation = input("Wat is je eindstation? : ")

    return eindstation


def omroepen_reis(stations, beginstation, eindstation):
    """Functie print beginstation/rangnummer, eindstation/rangnummer, afstand in aantal stations, ritpijst en reisoverzicht"""
    rang_beginstation = stations.index(beginstation)+1
    rang_eindstation = stations.index(eindstation)+1
    afstand = rang_eindstation - rang_beginstation
    prijs = afstand * 5


    print()
    print("Het beginstation " + beginstation + " is het " + str(rang_beginstation) + "e station in het traject.")
    print("Het eindstation " + eindstation + " is het " + str(rang_eindstation) + "e station in het traject.")
    print("De afstand bedraagt " + str(afstand) + " station(s).")
    print("De prijs van het kaartje is " + str(prijs) + " euro.")
    print()
    print("Jij stapt in de trein in: " + beginstation)

    while rang_beginstation < rang_eindstation-1:
        print(" - " + stations[rang_beginstation])
        rang_beginstation += 1

    print("Jij stapt uit in: " + eindstation)

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "\’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)