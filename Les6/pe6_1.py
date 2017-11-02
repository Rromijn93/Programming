def seizoen(maandnummer):
    if maandnummer in range(3, 6):
        print('lente')
    elif maandnummer in range(6, 9):
        print('zomer')
    elif maandnummer in range(9, 12):
        print('herfst')
    else:                   # 12 t/m 2
        print('winter')

seizoen(3)