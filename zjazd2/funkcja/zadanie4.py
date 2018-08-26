def formatuj(*napis, **znaczniki):
    napisy = '\n'.join((napis)
    napisy = napisy.replace($cena, str(5))
    return napisy


def test_formatuj_napis_bez_znacznikow():
    assert formatuj('Hello word') == 'Hello word'

def test_formatuj_napisy_bez_znacznikow():
    assert formatuj('Hello word', 'Robert') == 'Hello word Robert'

def test_formatuj_napisy_ze_znaczniem():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto',cena=10) == 'koszt 10 PLN\nkwota 10 brutto'