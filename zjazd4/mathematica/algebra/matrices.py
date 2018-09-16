def add_matrices(a,b):
    c = []
    for row_i in range(len(a)):
        row =[]
        for col_i  in range(len(a[row_i])):
            element = a[row_i][col_i] + b[row_i][col_i]
            row.append(element)
        c.append(row)

    return c





