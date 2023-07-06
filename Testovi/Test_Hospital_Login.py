import unittest
import time
from ast import Break
from asyncio.base_subprocess import WriteSubprocessPipeProto
from cgitb import text
from multiprocessing.sharedctypes import Value
from readline import insert_text
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PythonOrgSearch(unittest.TestCase):
  
    def setUp(self):
        print("start", time.time())

    def test_login(self):
        browser = webdriver.Firefox()
        browser.get('http://localhost:8080/')
        try:
            browser.maximize_window()
            sleep(2)

            Account=browser.find_element_by_xpath("//*[@id='account-menu']")
            Account.click()
            sleep(2)

            Signin=browser.find_element_by_xpath("//*[@id='login']")
            Signin.click()
            sleep(1)

            User=browser.find_element_by_xpath("//*[@id='username']")
            User.send_keys ('admin')
            User.click()

            Pass=browser.find_element_by_xpath("//*[@id='password']")
            Pass.send_keys ('admin')
            Pass.send_keys(Keys.ENTER)
            
            welcome_message=WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "home-logged-message")))

            assert welcome_message != None
            assert welcome_message.text == "You are logged in as user \"admin\"."

        finally:
            browser.quit()

    def tearDown(self):
        print("end", time.time())

if __name__ == "__main__":
    unittest.main()
