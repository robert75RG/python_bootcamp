"""
Napisz program zamieniający miejscami w zadanej
liście liczb element największy z najmniejszym.

"""

liczby = [5, 2, 1, 4, 3]
print("Przed: ", liczby)
i_min = None
i_max = None

# wyszukuję indeksy najmniejszego
# i największego elementu
for biezacy_index in range(len(liczby)):
    if i_min is None or liczby[biezacy_index] < liczby[i_min]:
        i_min = biezacy_index
    if i_max is None or liczby[biezacy_index] > liczby[i_max]:
        i_max = biezacy_index

# zamieniam miejscami elementy najmniejszy i największy

# tmp = liczby[i_min]
# liczby[i_min] = liczby[i_max]
# liczby[i_max] = tmp

liczby[i_min], liczby[i_max] = liczby[i_max], liczby[i_min]

print("Po: ", liczby)