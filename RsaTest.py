import unittest

import rsa_startK1


class MyTestCase(unittest.TestCase):
    def testPGCD(self):
        print('fick dich')
        self.assertEqual(1, rsa_startK1.pgcd(7,8))  # add assertion here

    def testCoPrime(self):

        self.assertEqual(True, rsa_startK1.isCoprime(3, 18980))


if __name__ == '__main__':
    unittest.main()
