# review by vica
import unittest
from ..ex7_only_str import only_str


class MyTestCase(unittest.TestCase):
    def test_only_str(self):
        """check there is not strings elements after only_str"""
        l = ["dfg", 1, 2, "sdf", "sdf", "dsfs", 5, 65, "gd"]
        only_str(l)
        for ele in l:
            self.assertEqual(type(ele), str)
        del l

    def test_not_valid_argument(self):
        """check if argument is not list"""
        self.assertRaises(TypeError, only_str, {})


if __name__ == '__main__':
    unittest.main()