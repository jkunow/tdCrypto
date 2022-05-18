import unittest

import rsa_startK1 as rsa


class MyTestCase(unittest.TestCase):
    def testPGCD(self):
        print('fick dich')
        self.assertEqual(1, rsa.pgcd(7,8))  # add assertion here

    def testCoPrime(self):
        self.assertEqual(True, rsa.isCoprime(3, 18980))
        self.assertEqual(False, rsa.isCoprime(9, 81))






if __name__ == '__main__':
    unittest.main()
