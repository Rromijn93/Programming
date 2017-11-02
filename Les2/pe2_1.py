letters=('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

letterlijst = list(letters)

letterlijst.sort()
a=letterlijst.count('A')
b=letterlijst.count('B')
c=letterlijst.count('C')
letAantal= [a, b, c]
print(letAantal)