def wiecej_niz(napis, liczba_powtorzen):
    wynik = set()
    for litera in napis:
        if napis.count(litera) > liczba_powtorzen:
             wynik.add(litera)
    return wynik



print(wiecej_niz('AAAA',3))
def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 1) == set()

def test_wiecej_niz_dla_nie_pustego_napisu():
    assert wiecej_niz('aaa',2)=={'a'}

