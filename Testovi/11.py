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

#browser = webdriver.Chrome(ChromeDriverManager().install())

browser = webdriver.Firefox()



browser.get('https://google.com')
browser.maximize_window()

browser.find_element(By.ID, "W0wltc").click()

#sleep(5)

#a = browser.find_elements_by_class_name("btn-link")
#for element in a:
    #attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    #print(attrs)

    #if element.get_attribute("data-di-id") == 'di-id-796c97cf-ae470ac4':
        #print ("nasao sam ga")
        #element.click()

#xbtn = browser.find_element(By.XPATH, "//button[@aria-label='close']")
#print (xbtn)


#depart_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dcep-afed358e1-6396-4a15-82be-6c4ea8fe9553-flm-flight-flightQuery.flightSegments[0].originCode']")))
#depart_from.click()
#depart_from.send_keys("Zurich")
#depart_from.send_keys(Keys.ENTER)

#going_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dcep-afed358e1-6396-4a15-82be-6c4ea8fe9553-flm-flight-flightQuery.flightSegments[0].destinationCode']")))
#going_to.click()
#going_to.send_keys("New York")
#search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH)))

#for results in search_results:

    #if "New York (JFK)" in results.text:
        #results.click()
        #break

#for date in all_dates:
    #if date.get_attribute("data-date") == "23/08/2022":
        #date.click()
        #Break
    #browser.find_element(By.XPATH, "//input[@value='Search Flights']").click()

    #pageLength = driver.excecute_script(
        #window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return))
   #match = False
    #while (match == False):
        #lastCount = pageLength

    

#navigate to travel Website
#provide going from location "Zurich"
#provide going to location "New York"
#click on "flight search button"
#Select the filter "1 stop"
#Verify that the filtered results show flights having only 1 stop