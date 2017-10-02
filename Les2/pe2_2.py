cijferICOR = 9
cijferPROG = 7
cijferCSN = 8
cijferLijst=[cijferICOR, cijferPROG, cijferCSN]
gemiddelde = sum(cijferLijst) / len(cijferLijst)
beloning = gemiddelde*30*len(cijferLijst)
overzicht = ('Mijncijfers (gemiddeld een '+str(gemiddelde)+') leveren een beloning van €'+str(beloning)+' op!')
print(overzicht)