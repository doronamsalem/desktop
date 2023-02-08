# review by vica
import unittest
from ..ex1_get_filename import file_name

class MyTestCase(unittest.TestCase):
    def test_file_name_valid(self):
        """test valid path"""
        self.assertTrue(file_name("/Users/doronamsalem/Desktop/demo.txt"))

    def test_file_name_notvalid(self):
        """test not valid path"""
        self.assertRaises(TypeError, file_name, 5)

    def test_path_not_exist(self):
        """test not exist path"""
        self.assertRaises(OSError, file_name, "a")


if __name__ == '__main__':
    unittest.main()
