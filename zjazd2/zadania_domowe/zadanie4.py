'''
Zaimplementuj funkcję zliczającą liczbę wystąpień poszczególnych słów w zadanym napisie.
Podpowiedź: do podzielenia napisu na słowa użyj metody split()
'''


def policz_slowa(tekst):
    temp = tekst.lower()
    temp = temp.split()
    slowa = {}

    for i in temp:
        if i in slowa:
            slowa[i] +=1

        else:
            slowa[i] =1

    return slowa


print(policz_slowa('Ala ma kota i kota ma ala'))