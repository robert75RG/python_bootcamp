znak={}

tekst = input('Podaj tekst: ')
for i in tekst.lower():
    #if i in znak:
    #   znak[i] += 1
    #else:
    #   znak[i] = 1 '''
    znak[i] = znak.get(i,0) +1

for i in znak:
    print(f'-litera {i} wystąpiła {znak[i]} razy')