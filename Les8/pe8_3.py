def code(invoerstring):
    nieuwe_code = ''
    for letter in invoerstring:
        nieuwe_letter = chr(ord(letter)+3)
        nieuwe_code += nieuwe_letter
    return nieuwe_code

print(code("RutteAlkmaarDen Helder"))