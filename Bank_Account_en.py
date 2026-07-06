import sys


class BankAccount:
    def __init__(self):
        self.__cpin = 1234
        epin = int(input('Enter your 4 digit Pin: \n'))
        if self.__cpin != epin:
            print('Invalid Pin')
            sys.exit()
        self.__bal = int(input('Enter Balance:\n'))

    def deposite(self):
        d_amount = int(input('Enter deposite amount:\n'))
        self.__bal += d_amount

    def withdraw(self):
        w_amount = int(input('Enter Withdrawl amount:\n'))
        if w_amount > self.__bal:
            print('Insufficient Balance!')
        else:
            self.__bal -= w_amount

    def get_balance(self):
        return self.__bal
    
b = BankAccount()

b.deposite()
b.withdraw()
print('Final Balance:',b.get_balance())



