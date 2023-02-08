import unittest
from Point import Point


class PointTest(unittest.TestCase):

    def setUp(self):
        """creating an object in test fixture"""
        self.p1 = Point(4, 8)

    def test_div_0(self):
        """check if division by 0 raise an error"""
        self.assertRaises(ZeroDivisionError, self.p1.__truediv__, 0)
        self.p1.__truediv__(2)
        self.assertEqual(self.p1.x, 2)
        self.assertEqual(self.p1.y, 4)

    def testMustBePoint(self):
        """is the Point class works"""
        self.assertRaises(TypeError, self.p1, Point)

    def testArgumentMustBeNumber(self):
        """check if numbers work"""
        self.assertRaises(TypeError, self.p1.x, "str")
        self.assertRaises(TypeError, self.p1.y, "str")



if __name__ == '__main__':
    unittest.main()


