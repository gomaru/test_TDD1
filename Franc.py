
class Franc:
    _amount=0
    def __init__(self,init_amount):
        self._amount = init_amount
    def times(self,multiplier):
        return Franc(self._amount*multiplier)
    def equals(self,franc):
        return self._amount == franc._amount