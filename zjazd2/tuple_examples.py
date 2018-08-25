imiona=('Robert', 'Kamil', 'Piotrek', 'Karolina', 'Kamil')
print(type(imiona))
print(imiona)
print(len(imiona))
print('Robert' in imiona)
print('Rafał' in imiona)

for imie in imiona:
    print(imie)

print(imiona[2])
print(imiona[-1])
print(imiona[:])
print('Indeks imienia Kamil to', imiona.index('Kamil'))
print('Powiedz ile razy wystąpiło imie Kamil to', imiona.count('Kamil'))