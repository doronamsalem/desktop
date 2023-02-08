# interview by vica
import unittest
from ..ex5_str_methods import str_dunder_filter, str_dunder_comp, str_dunder

class MyTestCase(unittest.TestCase):
    def test_comp(self):
        """test if returned list not contain dunder"""
        self.assertFalse("__" in str_dunder_comp())

    def test_filter(self):
        """test if returned list not contain dunder"""
        self.assertFalse("__" in str_dunder_filter())

    def test_dunder(self):
        """test if returned list not contain dunder"""
        self.assertFalse("__" in str_dunder())

if __name__ == '__main__':
    unittest.main()