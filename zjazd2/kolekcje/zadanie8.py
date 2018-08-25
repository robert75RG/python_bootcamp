tekst = 'Ala ma <kota>, a kot ma Alę'
''' 
z = tekst.find('<')
y = tekst.find('>')
print(len(tekst[z:y-1]))
'''
  #przy użyciu pętli for
czy_jest_pomiedzy_nawiasami = False

ile = 0
for i in tekst:
    if i == '<':
        czy_jest_pomiedzy_nawiasami = True
    elif i == '>':
        czy_jest_pomiedzy_nawiasami = False
    elif czy_jest_pomiedzy_nawiasami:
        ile += 1
print(ile)