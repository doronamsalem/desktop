# review by vica
import unittest
import os
from ..ex2_capital_file import make_capital_file

class MyTestCase(unittest.TestCase):
    def test_make_capital_file(self):
        """checks if the content is really capital"""
        file_path = "/Users/doronamsalem/Desktop/test_file_for_ex2.txt"
        with open(file_path, "w") as f1:
            f1.write("abcdefgaa")

        make_capital_file(file_path)

        with open(file_path, "r") as f2:
            content = f2.read()

        self.assertTrue(content.isupper())
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
