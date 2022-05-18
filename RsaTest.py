import unittest

import rsa_startK1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def testCoPrime(self):

        self.assertEqual(True, rsa_startK1.isCoprime(3, 18980))


if __name__ == '__main__':
    unittest.main()
