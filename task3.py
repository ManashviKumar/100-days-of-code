#autofill signup

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

#search firstname,lastname and email and enter details
fname=driver.find_element(By.NAME,"fName")
fname.click()
fname.send_keys("jdnjd")

lname=driver.find_element(By.NAME,"lName")
lname.click()
lname.send_keys("bffffff")

email=driver.find_element(By.NAME,"email")
email.click()
email.send_keys("jdnjd@gmail.com")

signup=driver.find_element(By.CSS_SELECTOR,value="form button")
signup.click()