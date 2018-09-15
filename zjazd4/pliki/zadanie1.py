import sys
try:
    wejscie = sys.argv[1]
    with open(wejscie, encoding='utf-8') as f:
        dane = f.read()
        dane = dane.splitlines()
        i = 0
        for i, linie in enumerate(dane, start=1):

            print(f'{i}:  {linie}')


except IndexError:
    print("Podaj nazwę pliku")
