import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        driver = self.driver
        driver.get('http://localhost:8081/2.html')
        assert 'My first web page' in driver.title 

    def test_click_button(self):
        driver = self.driver
        driver.get('http://localhost:8081/2.html')

        button = driver.find_element_by_id("button1")
        assert button
        button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    