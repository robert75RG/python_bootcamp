ile_podzielne = 0
podzielne_5 = 0

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        ile_podzielne += 1
        print(i)

print(f'Podzielnych przez 3 i 5 jest: {ile_podzielne}')
