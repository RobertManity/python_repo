from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://localhost:8081/1.html')
assert 'page' in browser.title

#elem = browser.find_element(By.NAME, 'p')  # Find the search box
#elem.send_keys('seleniumhq' + Keys.RETURN)

p = browser.find_element_by_id("hello")
assert p


print ("hello")

browser.quit()