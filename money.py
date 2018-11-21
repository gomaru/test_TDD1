from abc import *


class Money:
    _amount=0
    _currency = ""
    def __init__(self,amount, currency):
        self._amount = amount
        self._currency = currency
    def times(self,multiplier):
        return Money(self._amount*multiplier, self._currency)
    def currrency(self):
        return self._currency

    def equals(self,money):
        return self._amount == money._amount  and self._currency == money._currency

    def dollar(self,amount):
        return Dollar(amount,"USD")

    def franc(self,amount):
        return Franc(amount,"CHF")

class Dollar(Money):
    def __init__(self,amount,currency):
        super(Dollar,self).__init__(amount, currency)

class Franc(Money):
    def __init__(self,amount,currency):
        super(Franc,self).__init__(amount, currency)
