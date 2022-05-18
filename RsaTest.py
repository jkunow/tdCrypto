import unittest

import rsa_startK1 as rsa


class MyTestCase(unittest.TestCase):
    def testPGCD(self):
        self.assertEqual(1, rsa.pgcd(7,8))
        self.assertEqual(2, rsa.pgcd(4,2))
        

    def testCoPrime(self):
        self.assertEqual(True, rsa.isCoprime(3, 18980))
        self.assertEqual(False, rsa.isCoprime(9, 81))




        self.assertEqual(True, rsa.isCoprime(3, 18980))

    def testEuclideExt(self):
        self.assertEqual((1,27,-19987), rsa.euclide_ext(57000,77))



if __name__ == '__main__':
    unittest.main()
