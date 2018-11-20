
class Dollar:
    _amount=0
    def __init__(self,init_amount):
        self._amount = init_amount
    def times(self,multiplier):
        return Dollar(self._amount*multiplier)
    def equals(self,dollar):
        return self._amount == dollar._amount