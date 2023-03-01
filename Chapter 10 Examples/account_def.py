""" 
Alexandra Coffin
2023/2/28
Data Analytics Fundementals
Dr. Case

Account Class Def.
"""

from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initial. an Account Object."""

        if balance < Decimal('0.00'):
            raise ValueError('Inital balance must be >= 0.00.')
        
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Depositing funds into the account."""

        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        
        self.balance += amount
    
    def withdraw(self, amount):
        """Withdrawing money from funds"""

        #if amount is greater than balance, raise an exception.
        if amount > self.balance:
            raise ValueError('Amount must be <= to balance.')
        elif amount< Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        
        self.balance -= amount