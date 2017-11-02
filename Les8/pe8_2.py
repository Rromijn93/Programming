def monopolyworp():
    import random
    worpen = 0

    while worpen < 3:
        dobbelsteen1 = random.randrange(1, 7)
        dobbelsteen2 = random.randrange(1, 7)
        totaal = dobbelsteen1 + dobbelsteen2

        if worpen == 2 and dobbelsteen1 == dobbelsteen2:
            print(str(dobbelsteen1) + " + " + str(dobbelsteen2) + " = (direct naar de gevangenis)")
            worpen += 1
            break

        elif dobbelsteen1 != dobbelsteen2:
            print(str(dobbelsteen1) + " + " + str(dobbelsteen2) + " = " + str(totaal))
            break

        else:
            print(str(dobbelsteen1) + " + " + str(dobbelsteen2) + " = " + str(totaal) + " (dubbel)")
            worpen += 1


monopolyworp()