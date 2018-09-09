import math
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        '''
        new_x = self.x + other.x
        new_y = self.y+other.y
        Vector(new_x, new_y)
        '''
        v_ret = Vector(self.x + other.x, self.y+other.y)
        return v_ret

    def __sub__(self, other):
        v_ret = Vector(self.x - other.x, self.y - other.y)
        return v_ret

    def __mul__(self, other):
        v_ret = Vector(self.x * other, self.y * other)

        return v_ret
    @property
    def lenght(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.lenght == other.lenght


    def __gt__(self, other):
        return self.lenght > other.lenght
    def __gt__(self, other):
        return self.lenght >- other.lenght

    def __lt__(self, other):
        return self.lenght < other.lenght

    def __le__(self, other):
        self.lenght <= other.lenght
    def __ne__(self, other):
        return self.lenght != other.lenght
    def __str__(self):
        return f'V{self.x},{self.y}: {self.lenght}'



def test_create():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    assert v1.x == 1
    assert v1.y == 2

def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6

def test_sub():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v2 - v1
    assert v3.x == 2
    assert v3.y == 2

def test_mul():
    v1 = Vector(1, 2)
    x = 4
    v2 = v1 * x
    assert v2.x == v1.x * 4
    assert v2.y == v1.y * 4

def test_len():
    v1 = Vector(3,4)

    assert v1.lenght == 5

def test_equql():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    assert v1 == v2

def test_wiekszy_t():
    v1 = Vector(30, 4)
    v2 = Vector(3, 4)
    assert v1 > v2

def test_mniejsze_l():
    v1 = Vector(3, 4)
    v2 = Vector(10,4)
    assert v1 < v2

def test_rozne_l():
    v1 = Vector(3, 4)
    v2 = Vector(10,4)
    assert v1 != v2

def test_sort():
    v1 = Vector(1,2)
    v2 = Vector(0,1)
    v3 = Vector(3,2)
    listaV = [v1, v2, v3]
    assert sorted(listaV) == [v2,v1,v3]
    #print(listaV)


