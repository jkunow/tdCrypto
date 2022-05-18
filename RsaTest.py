import unittest

import rsa_startK1 as rsa


class MyTestCase(unittest.TestCase):
    def testCoPrime(self):
        self.assertEqual(True, rsa.isCoprime(3, 18980))
        self.assertEqual(False, rsa.isCoprime(9, 81))






if __name__ == '__main__':
    unittest.main()
