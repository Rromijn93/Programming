while True:
    string = input("Geef een string van vier letters: ")
    lengte = len(string)

    if lengte == 4:
        print()
        print("Inlezen van correcte string: " + string + " is geslaagd")
        break

    print(string + " heeft " + str(lengte) + " letters")
