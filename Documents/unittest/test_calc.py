import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        """ Calculate the sum """
        result = calc.add(10, 5)
        self.assertEqual(result, 13, "it is not correct")

    def test_add1(self):
        """ Calculate the  sum """
        result = calc.add(10, 5)
        self.assertEqual(result, 13, "it is not correct")

    def test_sub(self):
        """ Calculate the  sum """
        result = calc.subtract(0, 5)
        self.assertEqual(result, 13, "zero value as input")

if __name__ == '__main__':
    unittest.main()