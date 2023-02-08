# review by vica
import unittest
from ..ex9_list_to_dict import list_to_dict, list_to_dict1


class MyTestCase(unittest.TestCase):
    def test_not_list(self):
        """checks not valid data"""
        self.assertRaises(AssertionError, list_to_dict, {})
        self.assertRaises(AssertionError, list_to_dict, ())
        self.assertRaises(AssertionError, list_to_dict1, {})
        self.assertRaises(AssertionError, list_to_dict1, ())

    def test_dict_values(self):
        """check if the keys are indexes and values same as lists value"""
        l = [1, 2, 3, 4, 5]
        d = list_to_dict1(l)
        d_values = list(d.values())
        d_keys = list(d.keys())
        for x in range(len(l)):
            self.assertEqual(d_values[x], l[x])
            self.assertEqual(x, d_keys[x])


if __name__ == '__main__':
    unittest.main()
