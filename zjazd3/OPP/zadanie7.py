from zjazd3.OPP.zadanie2 import Employee


class PremiumEmployee(Employee):



    def __init__(self, name='Jan', lastname='Kowalski', wage=50, bonus = 0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    def give_bonnus(self, bonus):
        self.bonus += bonus


    def pay_salary(self):
        #sal = super(PremiumEmployee, self).pay_salary()
        sal = super().pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal

    @classmethod
    def creat_hearo(cls):
        return PremiumEmployee('pracownik','miesiąca', 0.0)

    @classmethod
    def em_from_string(cls, str_params):
        lista_param = str_params.split(',')
        return PremiumEmployee(lista_param[0], lista_param[1], int(lista_param[2]))

    @staticmethod
    def say_hello():
        return 'Hello'


def test_import_from_tekst():
    param = 'Henryk,Kania, 50'
    emp = PremiumEmployee.em_from_string(param)
    assert emp.name == 'Henryk'
    assert emp.lastname == 'Kania'
    assert emp.wage == 50


def test_creat_premium_employee():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 0


def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonnus(1000)
    emp.give_bonnus(400)
    assert emp.bonus == 1400
    assert emp.pay_salary() == 1900
'''
def test_employee_of_the_month()
    emp = PremiumEmployee.creat_hearo()

    assert emp.pay_salary == 0
'''