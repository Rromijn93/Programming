studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    """zet het gemiddelde per student in een lijst"""
    gemiddelde_studenten = []
    for student in studentencijfers:
        gemiddelde_studenten.append(sum(student) / len(student))
    return gemiddelde_studenten


def gemiddelde_van_alle_studenten(studentencijfers):
    """berekend te som aan de hand van de uitkomst bij gemiddelde_per_student"""

    totaal = sum(gemiddelde_per_student(studentencijfers))
    lengte = len(gemiddelde_per_student(studentencijfers))

    return totaal / lengte


print(gemiddelde_per_student(studentencijfers))
print(int(gemiddelde_van_alle_studenten(studentencijfers)))
