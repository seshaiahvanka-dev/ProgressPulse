from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display(self):
        print('Account:',self.account_number,'Balance:',self.balance)

class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposite(self, amount):
        self.balance += amount
        print('Deposited Amount:',amount,'New Balance:',self.balance)

    def withdraw(self, amount):
        if self.balance-amount >= 500:
            self.balance -= amount
            print('Withdrawl Amount:',amount,'New Balance:',self.balance)
        else:
            print('Insufficient Funds,Please Maintain minimum balance of 500')

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposite(self, amount):
        self.balance += amount
        print('Account:',self.account_number,'Balance:',self.balance)

    def withdraw(self, amount):
        if self.balance-amount >= -10000:
            self.balance -= amount
            print('Withdrawl Amount:',amount,'New Balance:',self.balance)
        else:
            print('Limit Exceeded,Overdraft cannot exceed -10000')

s = SavingsAccount('SA4HFU',2000)
c = CurrentAccount('CAHFI4NFH',5000)

s.deposite(1000)
s.withdraw(20000)
s.display()
c.withdraw(20000)
c.display()
