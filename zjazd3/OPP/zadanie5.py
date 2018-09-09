class CashMachine:
    def __init__(self):
        self._bills = dict()

    def is_available(self):
        return sum(self._bills.values()) > 0

    def put_money(self, list_of_money):
        for bill in list_of_money:
            self._bills[bill] = self._bills.get(bill, 0) + 1

    def withdraw(self, amount):

        list_of_bill = sorted(self._bills.keys(), reverse=True)
        ret_value = []
        for bill in list_of_bill:
            while self._bills[bill] > 0 and amount - bill >= 0:
                ret_value.append(bill)
                self._bills[bill] -= 1
                amount -= bill
        if amount == 0:
            return ret_value
        else:
            self.put_money(ret_value)
            return []
        return ret_value


def test_create():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()


def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()


def test_withdraw():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw(150) == [100, 50]



def test_withdraw_more_them_avaliable():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw(500) == []
    assert cash_machine.is_available()

def test_withdraw_bug_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 20, 20, 20, 20, 20])
    assert cash_machine.withdraw(100) == [50, 20, 20, 20, 20, 20]