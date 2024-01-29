import os
import pathlib
import unittest

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    def test_title(self):

        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")
    
    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("decrease")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")
        
    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
    

if __name__ = "__main__":
    unittest.main()
    