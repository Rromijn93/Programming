def standaardprijs(afstandKM):
    """Functie voor het berekenen van de standaard prijs"""
    prijsKM = 0.60
    prijsKM2 = 0.80
    if afstandKM <= 0:
        return 0
    elif afstandKM >= 50:
        return 15 + (afstandKM - 50) * prijsKM
    else:
        return afstandKM * prijsKM2


def ritprijs(leeftijd, weekendrit, afstandKM):
    """Functie voor het berekenen van de ritprijs"""
    prijs = standaardprijs(afstandKM)
    if weekendrit not in ['ja', 'Ja'] and (leeftijd < 12 or leeftijd >= 65):
        return prijs * 0.70
    elif weekendrit in ['ja', 'Ja'] and (leeftijd < 12 or leeftijd >= 65):
        return prijs * 0.65
    elif weekendrit in ['ja', 'Ja']:
        return prijs * 0.60
    else:
        return prijs


afstandKM = eval(input('Geef het aantal KM op: '))
leeftijd = eval(input('Geef de leeftijd op: '))
weekendrit = (input('Is de rit in het weekend?: '))

uiteindelijkeprijs = ritprijs(leeftijd, weekendrit, afstandKM)

print('€' + str(uiteindelijkeprijs))

# tests 3x24:

# test onder de 50km
# print(ritprijs(11, 'ja', 20))
# print(ritprijs(12, 'ja', 20))
# print(ritprijs(64, 'ja', 20))
# print(ritprijs(65, 'ja', 20))
# print(ritprijs(11, 'nee', 20))
# print(ritprijs(12, 'nee', 20))
# print(ritprijs(64, 'nee', 20))
# print(ritprijs(65, 'nee', 20))

# negatieve test
# print(ritprijs(11, 'ja', 0))
# print(ritprijs(12, 'ja', 0))
# print(ritprijs(64, 'ja', 0))
# print(ritprijs(65, 'ja', 0))
# print(ritprijs(11, 'nee', 0))
# print(ritprijs(12, 'nee', 0))
# print(ritprijs(64, 'nee', 0))
# print(ritprijs(65, 'nee', 0))

# test boven de 50km
# print(ritprijs(11, 'ja', 60))
# print(ritprijs(12, 'ja', 60))
# print(ritprijs(64, 'ja', 60))
# print(ritprijs(65, 'ja', 60))
# print(ritprijs(11, 'nee', 60))
# print(ritprijs(12, 'nee', 60))
# print(ritprijs(64, 'nee', 60))
# print(ritprijs(65, 'nee', 60))
