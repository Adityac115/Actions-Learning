# pylint: disable=missing-module-docstring
import unittest

from calculator import add, subtract, multiply, divide

class CalculatorTests(unittest.TestCase):
    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = multiply(2, 6)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = divide(15, 3)
        self.assertEqual(result, 5)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
