from ast import Break
from asyncio.base_subprocess import WriteSubprocessPipeProto
from cgitb import text
from multiprocessing.sharedctypes import Value
from threading import BrokenBarrierError
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Firefox()

#browser = webdriver.Chrome()



browser.get('https://learnix-eshop.herokuapp.com/')
browser.maximize_window()
sleep(2)

search = browser.find_element(By.XPATH, "//*[@id='search']")

input_filled = browser.find_element(By.XPATH, "//*[@id='search']")
input_filled.send_keys('Iphone')
input_filled.send_keys (Keys.ENTER)
browser.get_screenshot_as_file("Noga")


