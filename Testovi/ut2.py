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
    





    phones=browser.find_element_by_xpath("//a[text()='Phones & PDAs']")
assert(phones)
phones.click()

iphone=browser.find_element_by_xpath("//a[text()='iPhone']")
iphone.click()
sleep(2)

first_pic=browser.find_element_by_xpath("//ul[@class='thumbnails']/li[1]")
first_pic.click()
sleep(2)

next_click=browser.find_element_by_xpath("//button[@title='Next (Right arrow key)']")

for i in range(0,5):
    next_click.click()
    sleep(2)
#browser screenshot
browser.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

x_button=browser.find_element_by_xpath("//button[@title='Close (Esc)']")
x_button.click()
sleep(1)

quantity=browser.find_element_by_id("input-quantity")
quantity.click
sleep(1)

quantity.clear()
sleep(1)
quantity.send_keys('2')
sleep(1)

add_to_button=browser.find_element_by_id("button-cart")
add_to_button.click()

laptops=browser.find_element_by_xpath("//a[text()='Laptops & Notebooks']")
action=ActionChains(browser)
action.move_to_element(laptops).perform()
sleep(2)
laptops_2=browser.find_element_by_xpath("//a[text()='Show All Laptops & Notebooks']")
laptops_2.click()

HP=browser.find_element_by_xpath("//a[text()='HP LP3065']")
HP.click()
sleep(1)

add_to_button_2=browser.find_element_by_xpath("//button[@id='button-cart']")
add_to_button_2.location_once_scrolled_into_view
sleep(1)

calendar=browser.find_element_by_xpath("//i[@class='fa fa-calendar']")
calendar.click()
sleep(1)

next_click_calendar=browser.find_element_by_xpath("//th[@class='next']")
month_year=browser.find_element_by_xpath("//th[@class='picker-switch']")

while month_year.text != "December 2022":
    next_click_calendar.click()
sleep(2)

calendar_date=browser.find_element_by_xpath("//td[text()='31']")
calendar_date.click()
sleep(2)


add_to_button_2.click()
sleep(1)

go_to_cart=browser.find_element_by_id("cart-total")
go_to_cart.click()
sleep(1)

checkout=browser.find_element_by_xpath("//p[@class='text-right']/a[2]")
assert(checkout)
checkout.click()
sleep(1)

