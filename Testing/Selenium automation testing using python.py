from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select  

print("sample test case started") 

global driver

driver = webdriver.Chrome()  

driver.maximize_window()  

driver.get("https://mukeshsundar23.github.io/Worldwide-Covid-19-Tracking-Website/")
time.sleep(3)

select = Select(driver.find_element('id','countrySelected'))
time.sleep(3)

select.select_by_visible_text('India')
time.sleep(1)
driver.find_element("id","searchBtn").send_keys(Keys.ENTER)
time.sleep(3)
print("Covid Stats of India is displayed successfully !!")

select.select_by_visible_text('Australia')
time.sleep(1)
driver.find_element("id","searchBtn").send_keys(Keys.ENTER)
time.sleep(3)
print("Covid Stats of Australia is displayed successfully !!")

select.select_by_visible_text('France')
time.sleep(1)
driver.find_element("id","searchBtn").send_keys(Keys.ENTER)
time.sleep(3)
print("Covid Stats of France is displayed successfully !!")

select.select_by_visible_text('Japan')
time.sleep(1)
driver.find_element("id","searchBtn").send_keys(Keys.ENTER)
time.sleep(3)
print("Covid Stats of Japan is displayed successfully !!")

select.select_by_visible_text('Mexico')
time.sleep(1)
driver.find_element("id","searchBtn").send_keys(Keys.ENTER)
time.sleep(3)
print("Covid Stats of Mexico is displayed successfully !!")

driver.close()
print("Sample test case is completed")



