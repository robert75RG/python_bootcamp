'''
Zaimplementuj funkcję, która na podstawie podanej listy stworzy nową listę zawierającą tylko elementyoryginalnej kolekcji z podanego zakresu
'''


def filtruj(lista, start, stop):
    new_list = []
    for i in lista:
        if i >= start and i <= stop:
            new_list.append(i)
    return new_list


# test
print(filtruj([-2, 10, 0, 5, 1, 16, 9], 1, 5))
