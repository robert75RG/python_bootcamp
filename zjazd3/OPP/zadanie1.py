class Product():
    def __init__(self, id, name, price):
        self.name = name
        self.id = id
        self.price = price



    def print_info(self):
        print(f'"{self.name}", id: {self.id}, cena: {self.price} PLN')


def test_product_exist():
    product= Product('1', 'Woda', 10.99)

    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

def test_print_info(capsys):
    product = Product('1', 'Woda', 10.99)
    product.print_info()
    wyjscie = capsys.readouterr()
    out = wyjscie[0]
    assert out == '"Woda", id: 1, cena: 10.99 PLN\n'
