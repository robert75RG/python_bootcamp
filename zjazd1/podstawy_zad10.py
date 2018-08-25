
'''
if dzialanie == '+':
    print(f'Wynik = {liczba1 + liczba2}')
   
elif dzialanie == '-':
    print(f'Wynik = {liczba1 -liczba2}')
	
elif dzialanie == '*':
    print(f'Wynik = {liczba1 * liczba2}')
	
elif dzialanie == '/':
    print(f'Wynik = {liczba1 / liczba2}')
	
else:
    print('Zły wybór działania')
'''
def oblicz(dzialanie, arg1, arg2):

    if dzialanie == '+':
       return arg1 + arg2
    elif dzialanie == '-':
       return arg1 - arg2
    elif dzialanie == '*':
        return arg1 * arg2
    elif dzialanie == '/':
        return arg1 / arg2
    else:
        return None
		
		
try:		
    liczba1 = float(input('Podaj pierwszą liczbę: '))
    liczba2 = float(input('Podaj drugą liczbę: '))
    dzialanie = input('Podaj działanie: ')		
    wynik = oblicz(dzialanie, liczba1, liczba2)
    print(f'Wynik: {wynik}')
except Exeption as e:
    print('Nieznane działanie')
	
print('Koniec')