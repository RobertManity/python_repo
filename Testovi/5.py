from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()


browser.implicitly_wait(5)
browser.get('https://prometej-kikinda.ls.rs/rs/')

google_lang = browser.find_element(By.CLASS_NAME, "goog-te-menu-value")
google_lang.click()

french=browser.find_element(By.TAG_NAME,"td")
all_children_by_xpath = french.find_elements(By.XPATH,".//*")
print(all_children_by_xpath)
french.click()
assert("Maison" in browser.page_source)



