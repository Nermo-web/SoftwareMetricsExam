import unittest
from EvenOrOdd import *


class TestEvenOrOdd(unittest.TestCase):

 def testEven(self):

    self.assertTrue(isEven(6))
    self.assertFalse(isEven(9))

 def testArithmetic(self):
    #Failure example
    #Floating nums will fail most of the time.
    #AssertionError: 1.0 != 0.9999999999999999
    num = 0
    for i in range(0, 10): 
        num = num + 0.1
    self.assertEqual(1.0, num)
 
 def testOddWithNegative(self):
     #Testing odd with negative numbers
    self.assertTrue(isOdd(-3))
    self.assertFalse(isOdd(-4))

 def is_odd(n):
    """Test if the argument is odd"""
    return not isEven(n)

unittest.main()