import unittest

from money import Money,Dollar,Franc

class TestMoney(unittest.TestCase):
    """test class of Money
    """

    def test_Multiplication(self):
        """test method of Multiplication
        """
        five = Dollar(5)
#       テキストには以下で比較するようになっていたが、できる気がしないので、下記で代用
#       self.assertEquals(Money.Dollar(10), five.times(2) )
        self.assertTrue( Dollar(10).equals( five.times(2)) )
        self.assertTrue( Dollar(15).equals( five.times(3)) )

    def testEquality(self):
        self.assertTrue( Dollar(5).equals( Dollar(5) ) )
        self.assertFalse( Dollar(5).equals( Dollar(6) ) )
        self.assertTrue( Franc(5).equals( Franc(5) ) )
        self.assertFalse( Franc(5).equals( Franc(6) ) )
        self.assertFalse( Franc(5).equals( Dollar(5) ) )

    def test_FrancMultiplication(self):
        """test method of FrancMultiplication
        """
        five = Franc(5)
        self.assertTrue( Franc(10).equals( five.times(2)) )
        self.assertTrue( Franc(15).equals( five.times(3)) )

    def testCurrency(self):
        self.assertEquals("USD", Dollar(1).currrency() )
        self.assertEquals("CHF", Franc(1).currrency() )
        
if __name__ == "__main__":
    unittest.main()