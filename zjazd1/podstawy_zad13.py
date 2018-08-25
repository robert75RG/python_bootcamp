ILE_DNI = 7
i = 1
suma = 0
while i <= ILE_DNI:
    
    tem = float(input('Podaj temperaturę: '))
    suma += tem
    print(f'Bieżąca średnia: {suma/i:.2f}')
    i += 1
    
    
print(f'Średnia temperatura z tygodnia wynosi: {suma/ILE_DNI:.2f}')