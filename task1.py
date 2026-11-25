#webscrap date of upcoming event in dictionary form from this site "https://www.python.org/"

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
name=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events={}
for n in range(len(event)):
    events[n]={
        "time":event[n].text,
        "name":name[n].text,
    }
print(events)


driver.quit()