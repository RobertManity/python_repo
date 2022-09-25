from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()



browser.get('http://localhost:8081/7.html')

search = browser.find_element_by_link_text("Blic").click()
print(browser.current_url)
assert (browser.current_url=="https://www.blic.rs/")

capture_path="C:\Users\Public\Pictures"
browser.save_screenshot(capture_path)