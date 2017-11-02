def kwadraten_som(grondgetallen):
    for getal in grondgetallen:
        if getal < 0:
            grondgetallen.remove(getal)
    nieuw_grondgetallen = []
    for x in grondgetallen:
        nieuw_grondgetallen.append(x**2)
    return sum(nieuw_grondgetallen)

print(kwadraten_som([4, 5, 3, -81]))