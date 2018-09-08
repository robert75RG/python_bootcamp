class ElectricCar:
    def __init__(self, maxrange):
        self.maxrange = maxrange
        self.range = maxrange

    def drive(self, distance):

        if distance <= self.range:
            self.range = self.range - distance
            return distance
        else:
            drove = self.range
            self.range = 0
            return drove

    def charge(self):
        self.range = self.maxrange


def test_electric_car_initializaiton():
    car = ElectricCar(100)
    assert car.maxrange == 100


def test_electric_car_drive_below_max_range():
    car = ElectricCar(100)
    assert car.drive(70) == 70


def test_electric_car_drive_over_max_range():
    car = ElectricCar(100)
    assert 100 == car.drive(130)


def test_electric_car_drive_over_max_range_in_two_approaches():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30