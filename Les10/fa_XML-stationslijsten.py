import xmltodict
# lezen xml bestand
with open("stations.xml") as bestand:
    inhoud = xmltodict.parse(bestand.read())

station = inhoud['Stations']['Station']

# printen van alle stations de code en het type.
print("Dit zijn de codes en types van de 4 stations:")
for item in station:
    print("{:5} - {}".format(item['Code'], item['Type']))
print()

# printen van alle stations de code en synoniemen.
print("Dit zijn alle stations met één of meer synoniemen:")
for item in station:
    if item['Synoniemen'] is not None:
        print("{:5} - {}".format(item['Code'], item['Synoniemen']['Synoniem']))
    else:
        pass
print()

# printen van alle stations de code en de lange naam.
print("Dit is de lange naam van elk station:")
for item in station:
    print("{:5} - {}".format(item['Code'], item['Namen']['Lang']))
