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

    def test_deposit(self):
        assert self.a1.deposit(-4) is False
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == '$0.00'
        assert self.a1.deposit(-7.4) is False
        assert self.a1.deposit(10.2) is True

        
    def test_withdraw(self):
        assert self.a1.withdraw(-9) is False
        assert self.a1.withdraw(0) is False
        assert self.a2.get_balance() == '$629.17'
        assert self.a2.withdraw(7256.38) is False
        assert self.a2.withdraw(5) is True

