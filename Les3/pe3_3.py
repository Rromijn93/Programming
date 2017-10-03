leeftijd = eval(input('Geef je leeftijd: '))
nlPaspoort = input('In het bezit van een Nederlands paspoort: ')

if leeftijd >= 18 and nlPaspoort == 'ja':

    print('Gefeliciteerd, je mag stemmen!')

else:

    print('Helaas je mag niet stemmen')