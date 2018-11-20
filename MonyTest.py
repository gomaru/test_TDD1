import unittest
import Money

class TestMoney(unittest.TestCase):
    """test class of Money
    """

    def test_Multiplication(self):
        """test method of Multiplication
        """
        five = Money.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def testEquality(self):
        five1 = Money.Dollar(5)
        five2 = Money.Dollar(5)
        self.assertTrue(  Money.Dollar(5).equals(Money.Dollar(5) ) )
        self.assertFalse(  Money.Dollar(5).equals(Money.Dollar(6) ) )

if __name__ == "__main__":
    unittest.main()