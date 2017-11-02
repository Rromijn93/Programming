def ticker(filename):
    bestand = open(filename, 'r')
    inhoud = bestand.read()
    bestand.close()

    tickerlijst = inhoud.split('\n')
    tickerdict = {}

    for rij in tickerlijst:
        tickerdict[rij.split(':')[0]] = rij.split(':')[1]

    return tickerdict


def completes(string):
    """print bedrijfsnaam of ticker-symbool aan de hand van input"""
    bedrijven = ticker("ticker symbols.txt")

    for key, value in bedrijven.items():
        if value in string:
            return key
        elif key in string:
            return value
        else:
            return "Staat niet in het bestand.."

input_bedrijf = input('Enter Company name: ')
print("Ticker symbol: " + completes(input_bedrijf))

input_symbol = input('Enter Ticker symbol: ')
print("Company name: " + completes(input_symbol))

