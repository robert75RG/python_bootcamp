x = int(input('Podaj pierwszą współżędną: '))
y = int(input('Podaj drugą współżędną: '))


if 0<= x <=10 and 0<= y <=10:
    print('Gracz znajduje się w górnym lewym rogu')
elif 10 < x <= 91 and 0<= y <=10:
    print('Gracz znajduje się w górnej cześci')
elif 91< x <=100 and 0<= y <=10:
    print('Gracz znajduje się w górnym prawym rogu')
elif 0< x <=10 and 11<= y <=91:
    print('Gracz znajduje się w lewej cześci')
elif 10<= x <=91 and 11<= y <=91:
    print('Gracz znajduje się w centrum')
elif 91< x <=100 and 11<= y <=91:
    print('Gracz znajduje się w prawej cześci')
elif 0<= x <=9 and 91< y <=100:
    print('Gracz znajduje się w dolnym lewym rogu')
elif 10<= x <=91 and 91< y <=100: 
    print('Gracz znajduje się w dolna krawędz')
elif 91< x <=100 and 91< y <=100:
     print('Gracz znajduje się w dolna prawym rogu')
else:
    print('Poza planszą')