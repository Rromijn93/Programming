def reis_berekenen():
    """Functie voor het berekenen van de groepsreis prijs per persoon."""
    try:
        kosten_reis = 4356
        aantal_personen = eval(input("Hoeveel personen gaan er mee op reis?: "))
        if aantal_personen < 0:
            raise ValueError
        kosten_per_persoon = kosten_reis / aantal_personen
        print(kosten_per_persoon)
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
    except ValueError:
        print("Negatieve getallen zijn niet toegestaaan!")
    except NameError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except:
        print("Onjuiste invoer!")

reis_berekenen()