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

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://swiss.com')
browser.maximize_window()

browser.find_element(By.XPATH, "//*[@id='cm-acceptAll']").click()

sleep(5)

a = browser.find_elements_by_class_name("btn-link")
for element in a:
    attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    print(attrs)

    if element.get_attribute("data-di-id") == 'di-id-796c97cf-ae470ac4':
        print ("nasao sam ga")
        element.click()


