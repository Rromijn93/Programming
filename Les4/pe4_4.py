def new_password(oldpassword, newpassword):
    antwoord = (oldpassword != newpassword) and (len(newpassword) >= 6) and any(char.isdigit() for char in newpassword)
    return antwoord


print(new_password('wachtwoordoud', 'wachtwoordouder0'))
