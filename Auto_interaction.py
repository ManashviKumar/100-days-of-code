#click and type using selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# data=driver.find_elements(By.ID,value="mwDA")
# data[0].click()
 #OR
#finding element by link_text
# portal=driver.find_element(By.LINK_TEXT,"Content portals")
# portal.click()

#find search button by name
search_button=driver.find_element(By.CLASS_NAME,value="vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search.cdx-button__icon")
search_button.click()
#type desired text and enter
search=driver.find_element(By.NAME,"search")
search.send_keys("Python",Keys.ENTER)
