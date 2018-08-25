x = [12,34,12,-32,-78,2,-5,23,-100]
len(x)

liczby_dodatnie = 0
liczby_ujemne = 0
for liczba in x:
    if liczba > 0:
        liczby_dodatnie += 1
    elif liczba <0:
        liczby_ujemne += 1

print(f'W Liście jest {liczby_dodatnie} iczb ujemnych i {liczby_ujemne} liczb dodatnich')
