suma = 0
ile = 0

while True:
    liczba = input('Podaj kolejną liczbę całkowitą ')
    if liczba == 'koniec':
        break
    suma += int(liczba)
    ile += 1
    
    
    
    
    
print(f'\nSuma: {suma}, dodałeś: {ile} liczb, a ich średnia to: {suma/ile:.2f}')  
print('Koniec')