def convert(celsius):
    """Graden Celsius naar Fahrenheit"""
    return celsius * 1.8 + 32


def table():
    """Print tabel met Celsius en Fahrenheit in stappen van 10"""
    f = 'F'
    c = 'C'
    print('{:^6}{:^9}'.format(f, c))
    format_table = '{0:>5}{1:>8}'
    for celsius in range(-30, 40 + 1, 10):
        print(format_table.format(convert(celsius), float(celsius)))


table()
