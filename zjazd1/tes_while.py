while True:
    i = int(input('Podaj liczbę całkowitą: '))
    if i % 7 == 0:
        print(f'Podałeś liczbę {i}, która jest podzielna przez 7')
        break
    print('Podałeś liczbę niepodzielną przez 7')
print("Koniec")