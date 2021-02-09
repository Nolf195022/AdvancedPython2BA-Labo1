# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils
import math
class TestUtils(unittest.TestCase):
    def test_fact(self):
        utils.fact(9) = math.factorial(9)
        pass
    
    def test_roots(self):
        utils.roots(9) = 3
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
