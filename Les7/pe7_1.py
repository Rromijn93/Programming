getallen_lijst = []
while True:
    getal = eval(input("Geef een getal: "))
    aantal = len(getallen_lijst)
    som = sum(getallen_lijst)

    if getal == 0:
        print("Er zijn " + str(aantal) + " getallen ingevoerd, de som is: " + str(som))
        break

    getallen_lijst.append(getal)