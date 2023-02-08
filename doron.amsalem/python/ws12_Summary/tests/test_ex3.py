# interview by vica
import unittest
from ..ex3_prime_num import is_prime

class MyTestCase(unittest.TestCase):
    def test_not_number(self):
        """test insert not valid value"""
        self.assertRaises(TypeError, is_prime, "f")

    def test_prime_number(self):
        """test prime numbers"""
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_not_prime_number(self):
        """test not prime numbers"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(12))


if __name__ == '__main__':
    unittest.main()