lista = [x/10 for x in range(11)]
print(lista)

tupla = {(x, x**2, x**3) for x in range(-10,11)}

print(tupla)

napisy = ['AAAA', 'aaaa', 'dddd']

c = {x:len(x) for x in napisy}
print(c)

