from abc import *


class Money:
    _amount=0
    def __init__(self):
        _amount = 0
    @abstractmethod
    def times(self,multiplier):
        pass

    def equals(self,money):
        return self._amount == money._amount  and type(self) == type(money)

    def dollar(self,amount):
        return Dollar(amount)

    def franc(self,amount):
        return Franc(amount)

class Dollar(Money):
    def __init__(self,init_amount):
        self._amount = init_amount
    def times(self,multiplier):
        return Dollar(self._amount*multiplier)

class Franc(Money):
    def __init__(self,init_amount):
        self._amount = init_amount
    def times(self,multiplier):
        return Franc(self._amount*multiplier)