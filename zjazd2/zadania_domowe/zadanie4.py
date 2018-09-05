'''
Zaimplementuj funkcję zliczającą liczbę wystąpień poszczególnych słów w zadanym napisie.
Podpowiedź: do podzielenia napisu na słowa użyj metody split()
'''


def policz_slowa(tekst):
    #temp = tekst.split()
    slowa = {}

    for i in tekst.split():
        if i in slowa:
            slowa.get(i)
            slowa[i] = 1
        else:
            slowa[i] += 1


    return slowa


print(policz_slowa('ala ma kota i kota ma ala'))
