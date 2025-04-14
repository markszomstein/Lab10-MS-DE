import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################



def test_multiply(self):
    self.assertEqual(calculator.multiply(3, 4), 12)
    self.assertEqual(calculator.multiply(-2, 5), -10)
    self.assertEqual(calculator.multiply(0, 100), 0)

def test_divide(self):
    self.assertEqual(calculator.divide(2, 10), 5)
    self.assertEqual(calculator.divide(4, 20), 5)
    self.assertEqual(calculator.divide(1, 3), 3)

def test_log_invalid_argument(self):
    with self.assertRaises(ValueError):
        calculator.logarithm(0, 5)

def test_hypotenuse(self):
    self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
    self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5.0)
    self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

def test_sqrt(self):
    with self.assertRaises(ValueError):
        calculator.square_root(-9)
    self.assertAlmostEqual(calculator.square_root(16), 4.0)
    self.assertAlmostEqual(calculator.square_root(0), 0.0)

def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        calculator.divide(0, 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()