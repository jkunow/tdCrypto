import unittest

import rsa_startK1 as rsa


class MyTestCase(unittest.TestCase):
    def testPGCD(self):
        self.assertEqual(1, rsa.pgcd(7, 8))  # add assertion here

    def testCoPrime(self):
        self.assertEqual(True, rsa.isCoprime(3, 18980))
        self.assertEqual(False, rsa.isCoprime(9, 81))

    def testExpoModRapide(self):
        self.assertEqual(650, rsa.expo_modulaire_rapide(4334432, 543245, 4345))
        self.assertEqual(1728, rsa.expo_modulaire_rapide(3, 12, 4567876543456789))







if __name__ == '__main__':
    unittest.main()
