s = input('Podaj tekst do analizy: ')
#SAMOGLOSKI = ['a', 'e', 'i', 'o','u', 'y']
SAMOGLOSKI = 'a,e,i,o,u,y'
ile = 0

for i in s.lower():
    if i in SAMOGLOSKI:
        ile += 1

print(f'Samogłosek w podanym teksie jest: {ile}')
input('Aby zakończyć naciśnij Enter')