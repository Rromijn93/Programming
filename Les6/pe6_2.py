string_lijst = eval(input("Geef lijst met minimaal 10 strings: "))

nieuwe_lijst = []
for string in string_lijst:
    if len(string) == 4:
        nieuwe_lijst.append(string)

print("De nieuw-aangemaakte lijst met alle vier-letter strings is: ")
print(nieuwe_lijst)         #["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]