# review by vica
import unittest
from ..ex8_indexes import list_indexes, dict_keys


class MyTestCase(unittest.TestCase):
    def test_not_list(self):
        """check if argument not list"""
        self.assertRaises(AssertionError, list_indexes, {})
        self.assertRaises(AssertionError, list_indexes, ())


    def test_not_dict(self):
        """check if argument not dict"""
        self.assertRaises(AssertionError, dict_keys, [])
        self.assertRaises(AssertionError, dict_keys, ())


if __name__ == '__main__':
    unittest.main()
