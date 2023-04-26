

class Account:
    '''
    A class representing details for an account object
    '''
    
    def __init__(self, name: str) -> None:
        '''
        Function to create initial state of a account object.
        :param name : Account's name.
        '''
        self.__account_name: str = name
        self.__account_balance: float = 0
    
    def deposit(self, amount: float) -> bool:
        '''
        Method to deposit money to someone's account.
        :return: True if amount is above 0 dollars.
        :return: False if amount is 0 dollars or below.
        :param amount: Amount being deposited into someone's account.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount: float) -> bool:
        '''
        Method to withdraw money from someone's account.
        :return: True if amount is greater than or equal to someone's account balance.
        :return: False if amount is 0 dollars or below or amount is greater than someone's account balance.
        :param amount: Amount being withdrawn from someone's account.
        '''
        if amount <= 0:
            return False
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
    
    def get_balance(self) -> str:
        '''
        Method to access someone's account balance.
        :return: Someone's account balance in dollars.
        '''
        return f'${self.__account_balance:.2f}'
    
    def get_name(self) -> str:
        '''
        Method to access someone's name on account.
        :return: Someone's name on account.
        '''
        return self.__account_name
    
    
