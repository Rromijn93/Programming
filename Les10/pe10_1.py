import xmltodict

# XML bestnad inlezen en artikelnamen onder elkaar uitprinten
with open("artikelen.xml") as bestand:
    inhoud = xmltodict.parse(bestand.read())

artikel = inhoud['artikelen']['artikel']

for item in artikel:
    print(item['naam'])

