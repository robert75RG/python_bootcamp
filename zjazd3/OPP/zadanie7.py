from zjazd3.OPP.zadanie2 import Employee


class PremiumEmployee(Employee):

    def __init__(self, name='Jan', lastname='Kowalski', wage=100, bonus = 0):
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
