import unittest
from tests import *


def tests():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromModule(module_name))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    

if __name__ == "__main__":
    tests()
    