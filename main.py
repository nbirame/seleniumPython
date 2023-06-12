import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Test avec DriverChrom local
service_path = Service(executable_path="C:/Users/Pro/Documents/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_path)
driver.get("http://localhost:8069/web/login")
# 2 | setWindowSize | 1268x640 |
driver.set_window_size(1268, 640)
driver.implicitly_wait(300)
# 3 | click | id=login |
driver.find_element(By.ID, "login").click()
# 4 | type | id=login | birame.ndiaye@fongip.sn
driver.find_element(By.ID, "login").send_keys("username")
time.sleep(2)
# 5 | click | id=password |
driver.find_element(By.ID, "password").click()
# 6 | type | id=password | ndiaye236
driver.find_element(By.ID, "password").send_keys("password")
time.sleep(2)
# 7 | click | css=.btn-block |
driver.find_element(By.CSS_SELECTOR, ".btn-block").click()
time.sleep(3)
driver.find_element(By.ID, "result_app_2").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".o_list_button_add").click()
time.sleep(2)
driver.find_element(By.ID, "o_field_input_9").click()
driver.find_element(By.ID, "ui-id-13").click()
driver.find_element(By.ID, "o_field_input_16").click()
driver.find_element(By.ID, "ui-id-7").click()
driver.find_element(By.ID, "o_field_input_17").send_keys("Test 1")
time.sleep(3)
