def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def test_czy_jest_pierwsza_dla_liczb_pierwszych():
    assert czy_jest_pierwsza(3)

def test_czy_jest_pierwsza_dla_liczb_niepierwszych():
    assert not czy_jest_pierwsza(4)

'''
x = int(input('Podaj liczbę: '))
print(czy_jest_pierwsza(x))
'''
