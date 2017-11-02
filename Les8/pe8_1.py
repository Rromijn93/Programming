bruin = {"Borxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond \'t Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Borxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}

print("Overeenkomsten tussen groen en bruin: " + str(groen & bruin))
print("Plaatsen van traject bruin die niet door allebei aangedaan worden: " + str(bruin - groen))
print("Stations die worden van beide strajecten: " + str(bruin | groen))