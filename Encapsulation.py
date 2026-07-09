class AccountHolder:
    def __init__(self):
        self.__bal = 10000
    @property
    def bal(self):
        if self.__bal>0:
            return self.__bal
    @bal.setter
    def bal(self,amt):
        self.__bal = amt
    # bal = property(get_bal,set_bal)
ah = AccountHolder()
print(ah.bal)
ah.bal = 2000
print(ah.bal)

# print(ah._AccountHolder__bal)
# print(ah.get_bal())
# ah.set_bal(20000)
# print(ah.get_bal())
