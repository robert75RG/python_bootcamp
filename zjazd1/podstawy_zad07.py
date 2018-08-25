liczba = int(input('Podaj liczbę całkowitą: '))
x = liczba%2 == 0 and liczba%3==0 and liczba > 10 or liczba == 7
print(x)