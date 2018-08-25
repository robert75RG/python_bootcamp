'''i =0
while True:
    i += 1
    liczba = input('Podaj liczbę: ')
    
    if liczba == 'koniec':
        break
    temp = int(liczba)
    if i == 1:
        min = max = temp
    else:
    
        if max < temp:
            max = temp
        if min > temp:
            min = temp 
        
print(f'Wartość maksymalkna to: {max}')
print(f'Wartość minimalna to: {min}')
print('Koniec')
'''
min = max = None
while True:
        txt = input('Podaj kolejną wartośc: ')
        if txt == 'koniec':
            break
        # w tej wersji ignorujemy teksty nie będące liczbami
        try:
            liczba = int(txt)
            if max is None or liczba > max:
                max = liczba
            if min is None or liczba < min:
                min = liczba
        except Exception:
            pass

print(f'Maksimum: {max}')
print(f'Minimum: {min}')
    