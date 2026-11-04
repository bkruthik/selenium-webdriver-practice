from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/exp1.html")
time.sleep(2)
driver.find_element(By.NAME,'name').send_keys("Ram")
driver.find_element(By.NAME,'dob').send_keys("2003-09-15")
driver.find_element(By.NAME,'eid').send_keys("jds@gmail.com")
driver.find_element(By.NAME,'age').send_keys("41")
driver.find_element(By.NAME,'pass').send_keys("123!@#")
driver.find_element(By.NAME,'submit').click()
time.sleep(2)
driver.quit()