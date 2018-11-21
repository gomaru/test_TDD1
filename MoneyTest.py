import unittest

from money import Money,Dollar,Franc

class TestMoney(unittest.TestCase):
    """test class of Money
    """

    def test_Multiplication(self):
        """test method of Multiplication
        """
        self._fact = Money(0,None)
        five = self._fact.dollar(5)
#       テキストには以下で比較するようになっていたが、できる気がしないので、下記で代用
#       self.assertEquals(Money.Dollar(10), five.times(2) )
        self.assertTrue( self._fact.dollar(10).equals( five.times(2)) )
        self.assertTrue( self._fact.dollar(15).equals( five.times(3)) )

    def testEquality(self):
        self._fact = Money(0,None)
        self.assertTrue( self._fact.dollar(5).equals( self._fact.dollar(5) ) )
        self.assertFalse( self._fact.dollar(5).equals( self._fact.dollar(6) ) )
        self.assertTrue( self._fact.franc(5).equals( self._fact.franc(5) ) )
        self.assertFalse( self._fact.franc(5).equals( self._fact.franc(6) ) )
        self.assertFalse( self._fact.franc(5).equals( self._fact.dollar(5) ) )

    def test_FrancMultiplication(self):
        """test method of FrancMultiplication
        """
        self._fact = Money(0,None)
        five = self._fact.franc(5)
        self.assertTrue( self._fact.franc(10).equals( five.times(2)) )
        self.assertTrue( self._fact.franc(15).equals( five.times(3)) )

    def testCurrency(self):
        self._fact = Money(0,None)
        self.assertEquals("USD", self._fact.dollar(1).currrency() )
        self.assertEquals("CHF", self._fact.franc(1).currrency() )
    
#    def testDifferentClassEquality(self):
#        self.assertTrue(Money(10,"CHF").equals(Franc(10,"CHF")))
        

if __name__ == "__main__":
    unittest.main()