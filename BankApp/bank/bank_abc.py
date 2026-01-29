from abc import ABC, abstractmethod

class Bank(ABC):
    
    def __init__(self,name,balance=0):
        self.name=name
        self._balance=balance # protected

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def get_balance(self):
        return self._balance  
    
