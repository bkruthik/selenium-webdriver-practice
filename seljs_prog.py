from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("Link")

time.sleep(3)

driver.find_element(By.ID,'name').send_keys("Ram")
driver.find_element(By.ID,'submit').click()

time.sleep(3)
alt=driver.switch_to.alert
print("Alert The text" ,alt.text)

alt.accept()
print("IT is closed!!")

time.sleep(4)

driver.quit()
