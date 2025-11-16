# https://github.com/suak7/lab10-SA-BSM
# Partner 1: Sumeyya Aktas
# Partner 2: Bryan Sales-Mendez

import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-5, -2), -7)
        self.assertAlmostEqual(add(3.5, 3.2), 6.7)

    def test_subtract(self):
        self.assertEqual(subtract(15, 5), 10)
        self.assertEqual(subtract(-4, -1), -3)
        self.assertAlmostEqual(subtract(8.3, 5.4), 2.9)

    def test_multiply(self):
        self.assertEqual(mul(7, 3), 21)
        self.assertEqual(mul(-4, 8), -32)
        self.assertAlmostEqual(mul(4.1, 5.0), 20.5)

    def test_divide(self):
        self.assertEqual(div(20, 2), 10)
        self.assertEqual(div(-18, 6), -3)
        self.assertAlmostEqual(div(8, 5), 1.6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(math.e, math.e), 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 7)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(4.5, 1.5), math.hypot(4.5, 1.5))

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(5), math.sqrt(5))

        with self.assertRaises(ValueError):
            square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()