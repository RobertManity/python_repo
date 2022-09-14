import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        driver = self.driver
        driver.get('https://learnix-eshop.herokuapp.com')
        assert ' eShop' in driver.title 

    def test_click_button(self):
        driver = self.driver
        driver.get('https://learnix-eshop.herokuapp.com')

        search = driver.find_element_by_id("search")
        assert search
        search.click()

        search.send_keys("vr")

        lupa=driver.find_element_by_class_name("fa-search")
        lupa.click()

        div=driver.find_element_by_class_name("empty")
        print(div.text)
        assert div.text== "No products in database."
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()