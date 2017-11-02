def gemiddelde(zin):
    lengtes = []
    for woord in zin.split():
        lengtes.append((len(woord)))

    print(sum(lengtes) / len(lengtes))

gemiddelde(input('Geef een willekeurige zin op: '))