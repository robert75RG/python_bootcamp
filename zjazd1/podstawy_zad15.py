from random import randint, randrange
X_SKARB = randint(0,9)
Y_SKARB = randint(0,9)

x_gracza = randint(0,9)
y_gracza = randint(0,9)

ile_ruchow = 0
poczatkowa_odleglosc = abs(x_gracza - X_SKARB) + abs(y_gracza - Y_SKARB)
odl = poczatkowa_odleglosc


while True:
    odl = abs(x_gracza - X_SKARB) + abs(y_gracza - Y_SKARB)
    
    print(f'Znajdujesz się na pozycji x: {x_gracza}, y:{y_gracza}')
    if X_SKARB == x_gracza and Y_SKARB == y_gracza:
        print('Wygrałeś!!!')
    elif x_gracza > 10 or y_gracza >10:
        print('Jesteś poza planszą!!!')
    else:
        z = input('Podaj kierunek (w, s, d, a): ')
        if z == 'w':
            y_gracza -= 1
            
        elif z == 's':
            y_gracza += 1
            
        elif z == 'd':
            x_gracza += 1
            
        elif z == 'a':
            x_gracza -=1
        elif z == 'q':
            print('Poddajesz się? No dobra...')
        else:
            prin('Nie ma takiej komendy')
            continue
              
    ile_ruchow += 1       
    if x_gracza < 0  or x_gracza >10 or y_gracza < 0 or y_gracza > 10:
        
        print('Koniec gry spadłes z planszy')
        break
    if (x_gracza, y_gracza) == (X_SKARB, Y_SKARB):
        print(f'Wygrałeś!!! potrzebowałeś {ile_ruchow}')
        break
        
    if ile_ruchow > 2*poczatkowa_odleglosc:
        X_SKARB = randint(0,9)
        Y_SKARB = randint(0,9)
        ile_ruchow = 0
        poczatkowa_odleglosc = abs(x_gracza - X_SKARB) + abs(y_gracza - Y_SKARB)
        odl = poczatkowa_odleglosc
        
    nowa_odl = abs(x_gracza - X_SKARB)+abs(y_gracza - Y_SKARB)
    if randint(5) > 0:
        if nowa_odl< odl :
            print('Ciepło')
        else:
            print('Zimno')
    odl = nowa_odl
    
   
    
            
            