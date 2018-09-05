'''
Zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu.
Podpowiedź: rok przestępny to taki który dzieli się przez 4, ale nie dzieli się przez 100 lub dzieli się przez 400
'''


def lata_przestepne(start, stop):
    rok_prestepny = []
    for i in range(start, stop + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            rok_prestepny.append(i)
    return rok_prestepny


print(lata_przestepne(1990,2020))