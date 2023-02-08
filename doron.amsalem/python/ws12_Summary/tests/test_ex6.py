# review by vica
import unittest
from ..ex6_increment_list import increment_list

class MyTestCase(unittest.TestCase):

    def test_increment(self):
        """check if the sum of list in less by 1 for each element(list len)"""
        l = [x for x in range(5)]
        copy_list = l.copy()
        increment_list(l)
        self.assertEqual(sum(l), sum(copy_list) + len(l))
        self.assertNotEqual(sum(l), sum(copy_list))


if __name__ == '__main__':
    unittest.main()
