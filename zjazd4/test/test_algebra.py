from mathematica.algebra.matrices import add_matrices, sub_matrices

def test_add_matrices():
    a = [
        [1,2,3],
        [4,5,6]
    ]

    b = [
        [7,8,9],
        [10,11,12]
    ]
    result = matrices.add_matrices(a,b)
    expected=[
        [8, 10,12],
        [14, 16, 18]
    ]

    assert result == expected

def test_sub_matrices():
    a = [
        [1,2,3],
        [4,5,6]
    ]

    b = [
        [7,8,9],
        [10,11,12]
    ]
    result = matrices.sub_matrices(a,b)
    expected=[
        [-6, -6, -6],
        [-6, -6, -8]
    ]

    assert result == expected