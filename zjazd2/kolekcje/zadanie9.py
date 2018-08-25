'''
towar={'cukier': 3.15, 'mąka': 2.5, 'mleko': 1.95, 'chleb' : 2.56}
magazyn
koszyk = {}

for p in towar:
    print(f'-{p} - {towar[p]}: PLN')
while True:
    jaki_produkt = input('Co chcesz kupić: ')
    if jaki_produkt == 'k':
        break
    ile = float(input(f'Ile chcesz kupić {jaki_produkt}'))
    koszyk[jaki_produkt] = ile*towar[jaki_produkt]
koszt_calkowity = 0
for vCard in koszyk:
    koszt_calkowity += koszyk(vCard)
    print(f'Koszt: {vCard} - {ile*towar[jaki_produkt]}')
'''
produkty = {
    'ziemniaki': 1.99,
    'bataty': 6.99,
    'pomidory': 2.5,
    'piwo': 7
}

koszyk = {}


for p in produkty:
    print(f"- {p} - {produkty[p]} PLN ")


while True:
    #ścieszka zakupów
    komenda = input("Co chcesz zrobić: dodaj/kup")
    if komenda == 'kup':
        jaki_produkt = input("Jaki produkt chcesz kupić (wpisz k by zakończyć)? ")
        if jaki_produkt == 'k':
            print(koszyk)
            break
        ile = float(input(f"Ile chcesz kupić: {jaki_produkt}? "))
        koszyk[jaki_produkt] = ile*produkty[jaki_produkt]
    elif komenda == 'dodaj':
        pass
    else:
        print('Zły wybór')
for wklad in koszyk:
    print(f" - Koszt - {wklad} - {koszyk[wklad]}")
