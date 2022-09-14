from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Firefox()


browser.implicitly_wait(5)
browser.get('https://blic.rs')

pretraga = browser.find_element(by=By.ID, value='search-open')


pretraga.click()



input_filled = browser.find_element(by=By.ID, value='search-input')


input_filled.send_keys('Danas')

input_filled.send_keys(Keys.ENTER)

rezultat = browser.find_element(by=By.XPATH, value='/html/body/main/section/div/div/section[1]/article[1]/div[1]/a/figure/picture/img')

print(rezultat.text)


#search.send_keys('hayabusa',Keys.ENTER)

#search_instead=browser.find_element_by_css_selector("a-size-base a-color-base s-underline-text")
#print(search_instead)




