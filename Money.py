
class Dollar:
    amount=0
    def __init__(self,init_amount):
        self.amount = init_amount
    def times(self,multiplier):
        return Dollar(self.amount*multiplier)
    def equals(self,dollar):
        return self.amount == dollar.amount