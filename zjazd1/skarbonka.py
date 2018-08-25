skarbonka = 0

while skarbonka < 100:
    wplata = int(input('Ile wpłacasz? '))
    skarbonka += wplata
    print(f'Aktualnie w skarbonce jest: {skarbonka}')
    
print('Koniec')