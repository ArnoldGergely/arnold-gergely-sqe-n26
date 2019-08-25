import sys
import unittest
from automation.tests.test_best_buy import TestBestBuy


def suite():
    # initiating test suite
    suite_x = unittest.TestSuite()
    # adding the test files to test
    # task 3
    suite_x.addTest(unittest.makeSuite(TestBestBuy))
    return suite_x


def run():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    run()
