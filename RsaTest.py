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


    def testExpoModRapide(self):
        self.assertEqual(650, rsa.expo_modulaire_rapide(4334432, 543245, 4345))
        self.assertEqual(1728, rsa.expo_modulaire_rapide(3, 12, 4567876543456789))


    def testEuclideExt(self):
        self.assertEqual((1,37,-3), rsa.euclide_ext(13,160))
        self.assertEqual((1,27,-19987), rsa.euclide_ext(57000,77))
        self.assertEqual((3,0,1), rsa.euclide_ext(6,3))
        self.assertEqual((3,0,1), rsa.euclide_ext(0,3))
        self.assertEqual((4,1,0), rsa.euclide_ext(4,0))

    def testInverseMod(self):
        #self.assertEqual(1, rsa.inverse_modulaire(7,8))
        #self.assertEqual(2, rsa.pgcd(4,2))
    



if __name__ == '__main__':
    unittest.main()
