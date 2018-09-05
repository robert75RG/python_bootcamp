'''
Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo odlewej, jak i od prawej).
Podpowiedź: do odwrócenia napisu możemy wykorzystać mechanizm wycinania (ang. slicing).
'''


def czy_palindrom(tekst):
    temp = tekst[::-1]

    if temp == tekst:
        return True
    else:
        return False


# test

print(czy_palindrom('kajak'))

print(czy_palindrom('koń'))
print(czy_palindrom('mannam'))
print(czy_palindrom('121'))
