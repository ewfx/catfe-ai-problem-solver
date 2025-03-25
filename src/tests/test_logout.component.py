from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://localhost:4200')

#Login
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login").click()

time.sleep(2) #Allow time for page load

#Logout
logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']")))
logout_button.click()

time.sleep(2) #Allow time for page load

#Verification -  Assuming successful logout redirects to login page. Adapt as needed based on your application's behavior.
try:
    login_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    print("Logout successful")
except:
    print("Logout failed")

driver.quit()
