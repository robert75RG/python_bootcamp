import datetime


wiek_user = int(input('Podaj rok urodzenia: '))
rok_biezacy = datetime.datetime.today().year

wiek = rok_biezacy-wiek_user
if wiek >= 18:
    print('Jesteś pełnoletni')
else:
    print('Jesteś osobą niepełnoletnią')
'''
if 2018 - wiek_user >= 18:
    print('Jesteś pełnoletni!')
else:
    print('Jesteś niepełnoletni!')
'''