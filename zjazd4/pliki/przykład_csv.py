import csv

with open("pliki_wejsciowe/plik.csv") as f:
    dane = csv.DictReader(f)
    # print(dane)
    suma = 0
    i =0

    for row in dane:

        suma += float(row["Gross margin"])
        i += 1
    srednia = suma/i
    print(srednia)
