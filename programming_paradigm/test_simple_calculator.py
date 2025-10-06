import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 2), 7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_division(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertIsNone(self.calc.divide(5, 0))
