from money import Money

class Franc(Money):
    def __init__(self,init_amount):
        self._amount = init_amount
    def times(self,multiplier):
        return Franc(self._amount*multiplier)