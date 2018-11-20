import unittest
import Money

class TestMoney(unittest.TestCase):
    """test class of Money
    """

    def test_Multiplication(self):
        """test method of Multiplication
        """
        five = Money.Dollar(5)
        self.assertTrue(Money.Dollar(10).equals( five.times(2)) )
        self.assertTrue(Money.Dollar(15).equals( five.times(3)) )

    def testEquality(self):
        self.assertTrue(  Money.Dollar(5).equals(Money.Dollar(5) ) )
        self.assertFalse(  Money.Dollar(5).equals(Money.Dollar(6) ) )

if __name__ == "__main__":
    unittest.main()