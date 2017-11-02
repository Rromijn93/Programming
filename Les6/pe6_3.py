invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
splitlijst = invoer.split('-')
splitlijst.sort()

maxg = max(splitlijst)
ming = min(splitlijst)
totaal = 0
for num in splitlijst:
    totaal += int(num)
lengte = len(splitlijst)

print("Gesorteerde list van ints: " + str(splitlijst))
print("Grootste getal: " + maxg + " en Kleinste getal: " + ming)
print("Aantal getallen: " + str(lengte) + " en Som van de getallen: " + str(totaal))
print("Gemiddelde: " + str((totaal / lengte)))
