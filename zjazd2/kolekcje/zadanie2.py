
x=[]

while len(x) < 10:

    nowa_liczba = input("Podaj liczbę lub k by zakończyć")
    if nowa_liczba == 'k':
        break
    else:
        nowa_liczba = int(nowa_liczba)
        x.append(nowa_liczba)
    



print(f'Średnia wprowadzonych licz {sum(x)/len(x)}')

input('Jeśli chcesz zakończyć program naciśnij Enter')