with open('pliki_wejsciowe/dane.txt', encoding='utf-8') as plik:
    print(plik)
    print(plik.read())

with open('pliki_wejsciowe/nowy_plik.txt', 'a', encoding='utf-8') as f:
    f.write('ala ma kota')