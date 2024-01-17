from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
import time 
import pandas as pd

temp_list = []

driver = webdriver.Chrome()
# ...

driver.get("https://finance.yahoo.com/screener/equity/new")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
#cookie_button = driver.find_element("name", "q")
ele_accept_cookies_botton = driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[2]/div[2]/button[1]")
time.sleep(2)
ele_accept_cookies_botton.click()
time.sleep(2)
#element2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[2]/div/div/svg")
#time.sleep(2)
#element2.click()
time.sleep(2)
ele_mega_cap_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[4]")
time.sleep(2)
ele_mega_cap_button.click()
time.sleep(2)
ele_lrg_cap_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[3]")
time.sleep(2)
ele_lrg_cap_button.click()

time.sleep(2)
ele_search_stocks_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[2]/div[1]/div[3]/button[1]")
time.sleep(2)
ele_search_stocks_button.click()
time.sleep(2)
ele_show_more_rows = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[2]/span/div/span/span")
time.sleep(2)
ele_show_more_rows.click()
time.sleep(2)
ele_show_100_rows = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[2]/span/div/span/span")
time.sleep(2)
ele_show_100_rows.click()
time.sleep(2)


ele_fiance_table = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table")



for x in range (0,69,1):
    for row in range(1, 25):
        #print("row is: ", row)
        rows = ele_fiance_table.find_elements(By.XPATH, "//body//tbody//tr[" + str(row) + "]")
        #print("rows is: ", rows)
        for row_data in rows:
            #print("row_data is:", row_data)
            col = row_data.find_elements(By.TAG_NAME, "td")
            #print("col is: ", col)
            temp_list.append(col[0].text)
            #for i in range(len(col)):
                #print(col[i].text)
            
    time.sleep(2)
    #print (x)
    ele_next_page_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[2]/button[3]")
    time.sleep(2)
    ele_next_page_button.click()
    time.sleep(2)




print(temp_list)
df = pd.DataFrame(temp_list, columns = ['Tickers'])
df.to_csv('ticker_list', encoding='utf-8') 

#...
driver.quit()

