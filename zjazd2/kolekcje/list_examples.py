imiona=['Robert', 'Kamil', 'Piotrek', 'Karolina', 'Kamil']

print(type(imiona))
print(imiona)
print(len(imiona))
print('Robert' in imiona)
print('Rafał' in imiona)


#---------Różnice względem Tupli -------------
print(imiona)
imiona.append('Rafał')
imiona.append('Rafał')
imiona.append('Rafał')
print(imiona)

imiona.pop()
print(imiona)
print(imiona.pop())
imiona.remove('Rafał')
print(imiona)