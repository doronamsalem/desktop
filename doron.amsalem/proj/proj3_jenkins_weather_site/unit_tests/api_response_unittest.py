import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ApiResponse(unittest.TestCase):
    """unit test proper api response for valid and not valid """

    def setUp(self):
        """creating website request"""
        self.driver = webdriver.Safari()
        self.website_url = "http://localhost:80"
        self.driver.get(self.website_url)

    def teardown_module(self):
        self.driver.close()

    def test_input_israel(self):
        """test valid input of location"""
        location_input = self.driver.find_element("id", "location")
        location_input.send_keys("israel")
        location_input.submit()
        time.sleep(2.5)
        self.assertTrue(self.driver.title == "weather")
"""
    def test_input_other_language_israel(self):
        """test valid input of location"""
        location_input = self.driver.find_element("id", "location")
        location_input.send_keys("ישראל")
        location_input.submit()
        time.sleep(2.5)
        self.assertTrue(self.driver.title == "weather")

    def test_input_mix_letters(self):
        """test valid input of location"""
        location_input = self.driver.find_element("id", "location")
        location_input.send_keys("tOKyO JapAn")
        location_input.submit()
        time.sleep(2.5)
        self.assertTrue(self.driver.title == "weather")
"""
    def test_not_valid_input(self):
        """test valid input of location"""
        location_input = self.driver.find_element("id", "location")
        location_input.send_keys("sfsdetgd")
        location_input.submit()
        time.sleep(2.5)
        self.assertFalse(self.driver.title == "weather")


if __name__ == '__main__':
    unittest.main()
