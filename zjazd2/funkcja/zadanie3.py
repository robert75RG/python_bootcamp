def policz_znaki(napis,start='<', stop='>'):
    if start == stop:
        raise ValueError('Błąd, podane znaki są takie same.')

    ile_znakow = 0
    poziom = 0
    for litera in napis:
        if litera == start:
            poziom += 1
        elif litera ==stop:
            poziom -= 1
        elif poziom > 0:
            ile_znakow += poziom

    return ile_znakow


def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki('') == 0
    #assert policz_znaki("") == 0
def test_policz_znaki_gdy_brak_znakow():
    assert policz_znaki('Ala ma kota') == 0

def test_polcz_znaki_z_nawiasami():
    assert policz_znaki('Ala <ma> kota') == 2

def test_policz_znaki_z_innymi_separatorami():
    assert policz_znaki('Ala [kota [a]] ma [kota]', '[',']') == 11

'''
def dodaj(a,b):
    if type(b) == 'str':
        a = str(a)
    return a+b

def test_dodaj():
    assert dodaj(1,2) == 3
    assert dodaj(1,-1) == 0
    assert dodaj(1,'a') == '1a'
'''