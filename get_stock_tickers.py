from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
import time 


driver = webdriver.Chrome()
# ...

driver.get("https://finance.yahoo.com/screener/equity/new")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
#cookie_button = driver.find_element("name", "q")
element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[2]/div[2]/button[1]")
time.sleep(2)
element.click()
time.sleep(2)
#...
driver.quit()

