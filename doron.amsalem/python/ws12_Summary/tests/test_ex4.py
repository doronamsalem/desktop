# review by vica
import unittest
from ..ex4_square_add import square, add

class MyTestCase(unittest.TestCase):

    def test_square(self):
        """valid arguments"""
        self.assertEqual(square(6), 36)
        self.assertEqual(square(9), 81)

        self.assertNotEqual(square(6), 4)
        self.assertNotEqual(square(9), 80)

    def not_valid_sqr(self):
        """not valid arguments"""
        self.assertRaises(TypeError, square, "g")

    def test_add(self):
        """valid arguments"""
        self.assertEqual(add(9, 5), 14)
        self.assertEqual(add(0, -5), -5)

        self.assertNotEqual(add(9, 5), 10)
        self.assertNotEqual(add(0, -5), 5)

    def not_valid_add(self):
        """not valid arguments"""
        self.assertRaises(TypeError, add, ("g", 5))
        self.assertRaises(TypeError, add, (5, "r"))


if __name__ == '__main__':
    unittest.main()
