
'''
zbior =set()
ile = 0
while True:
    liczba = input('Podaj liczbę, jeśli chcesz zakończyć wpisz "stop"')
    if liczba == 'stop':
        break
    else:
        zbior.add(int(liczba))

for i in zbior:
    if i%2 and i <= 100:
        ile += 1
print(f'W zbiorze jest: {len(zbior)}, parzystych i mniejszych od 100 jest: {ile}')
'''
liczby =set()
while True:
    komenda = input('Podaj liczbę, jeśli chcesz zakończyć wpisz k')
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))
print(f'Wprowadzono {len(liczby)} liczb')
liczba_parzsta = set(range(2,101,2))
print(f'W tym parzystych z zakresu 0 - 100 jest {len(liczba_parzsta & liczby)}')