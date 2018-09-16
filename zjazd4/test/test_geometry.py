from mathematica.geometry.figures import squere_area, triangle_area

def test_squer_area():

    assert squere_area(4) == 16

def test_triangle_area():
    assert triangle_area(2,2) == 2