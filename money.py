from abc import *


class Money:
    _amount=0
    _currency = ""
    def __init__(self,amount, currency):
        self._amount = amount
        self._currency = currency
    @abstractmethod
    def times(self,multiplier):
        pass
    def currrency(self):
        return self._currency

    def equals(self,money):
        return self._amount == money._amount  and type(self) == type(money)

    def dollar(self,amount):
        return Dollar(amount)

    def franc(self,amount):
        return Franc(amount)

class Dollar(Money):
    def __init__(self,amount):
        super(Dollar,self).__init__(amount, "USD")
    def times(self,multiplier):
        return self.dollar(self._amount*multiplier)

class Franc(Money):
    def __init__(self,amount):
        super(Franc,self).__init__(amount, "CHF")

    def times(self,multiplier):
        return self.franc(self._amount*multiplier)
