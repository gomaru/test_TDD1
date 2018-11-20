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
        self.assertTrue( Money().dollar(10).equals( five.times(2)) )
        self.assertTrue( Money().dollar(15).equals( five.times(3)) )

    def testEquality(self):
        self.assertTrue(Money().dollar(5).equals( Money().dollar(5) ) )
        self.assertFalse(Money().dollar(5).equals( Money().dollar(6) ) )
        self.assertTrue(Money().franc(5).equals( Money().franc(5) ) )
        self.assertFalse(Money().franc(5).equals( Money().franc(6) ) )
        self.assertFalse(Money().franc(5).equals( Money().dollar(5) ) )

    def test_FrancMultiplication(self):
        """test method of FrancMultiplication
        """
        five = Franc(5)
        self.assertTrue( Money().franc(10).equals( five.times(2)) )
        self.assertTrue( Money().franc(15).equals( five.times(3)) )

if __name__ == "__main__":
    unittest.main()