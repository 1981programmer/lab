import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')
        self.a2.deposit(629.17)
        
    def teardown_method(self):
        del self.a1
        del self.a2
    
    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-4) is False
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(-7.4) is False
        assert self.a1.deposit(10.2) is True
        assert self.a1.get_balance() == 10.2
        
    def test_withdraw(self):
        assert self.a1.withdraw(-9) is False
        assert self.a1.withdraw(0) is False
        assert self.a2.get_balance() == 629.17
        assert self.a2.withdraw(7256.38) is False
        assert self.a2.withdraw(58.31) is True
        assert self.a2.get_balance() == pytest.approx(570.86, abs=0.001)

