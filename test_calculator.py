# https://github.com/markszomstein/Lab10-MS-DE.git
# Partner 1: Mark Szomstein
# Partner 2: Devon Elmes

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(-5,10), 5, "Testing add with neg and pos int")
        self.assertEqual(add(-2, -9), -11, "Testing add with two neg ints")
        self.assertEqual(add(100,0.25), 100.25, "Testing add with pos int and float")

    def test_subtract(self): # 3 assertions
    	self.assertEqual(subtract(-5, 10), -15, "Testing subtract with neg and pos int")
        self.assertEqual(subtract(-2, -9), 7, "Testing subtract with two neg ints")
        self.assertEqual(subtract(100, 0.25), 99.75, "Testing subtract with pos int and float")
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, -4)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(5,125), 3)
        self.assertAlmostEqual(logarithm(3,81), 4)
        self.assertAlmostEqual(logarithm(2,32), 5)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,125)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
