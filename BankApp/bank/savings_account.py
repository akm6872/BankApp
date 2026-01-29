from bank.bank_abc import Bank
from db.database import Database
from .exceptions import InsufficientFundsError

class SavingsAccount(Bank):

    def __init__(self,name,balance=0):
        super().__init__(name,balance)
        self.db = Database()
    
    def deposit(self,amount):
        self._balance += amount
        self.db.update_balance(self.name,self._balance)
        print(f"{amount} has been deposited and new available balance is {self._balance}")
    def withdraw(self,amount):
        if amount>self._balance:
            raise InsufficientFundsError(Exception)
        else:
            self._balance -= amount
            self.db.update_balance(self.name,self._balance)
            print(f"{amount} has been withdrawn and new available balance is {self._balance}")

        
