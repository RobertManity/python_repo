from ast import Break
from asyncio.base_subprocess import WriteSubprocessPipeProto
from cgitb import text
from multiprocessing.sharedctypes import Value
from threading import BrokenBarrierError
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Firefox()

#browser = webdriver.Chrome()


#Browser open the page
browser.get('http://tutorialsninja.com/demo/')
browser.maximize_window()
sleep(2)

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

