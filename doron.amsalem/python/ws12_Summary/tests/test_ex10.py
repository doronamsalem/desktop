# review by basheer
import unittest
from ..ex10_default_dict import DEFUALT_DICT

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """create new default dictionary"""
        self.d = DEFUALT_DICT(0)
        self.d["b"] = "s"

    def test_return(self):
        """check if list return value or default"""
        self.assertEqual(self.d["b"], "s")
        self.assertEqual(self.d["qwew"], self.d.default_key)



if __name__ == '__main__':
    unittest.main()