from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ui_context = {'module': 'register.component', 'ui_elements': [{'name': 'username_field', 'selector': "//*[@id='username']", 'type': 'input', 'placeholder': 'Enter your username', 'required': True}, {'name': 'password_field', 'selector': "//*[@id='password']", 'type': 'input', 'placeholder': 'Enter your password', 'required': True}, {'name': 'register_button', 'selector': "//button[@type='submit']", 'type': 'button', 'text': 'Register'}], 'test_cases': [{'scenario': 'Valid Registration', 'username': 'validuser', 'password': 'validpassword', 'expected': 'Registration successful'}, {'scenario': 'Invalid Registration - Missing Username', 'username': '', 'password': 'validpassword', 'expected': 'Username is required'}, {'scenario': 'Invalid Registration - Missing Password', 'username': 'validuser', 'password': '', 'expected': 'Password is required'}]}

driver = webdriver.Chrome()
driver.get('http://localhost:4200')

def register(username, password, expected):
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ui_context['ui_elements'][0]['selector'])))
    password_field = driver.find_element(By.XPATH, ui_context['ui_elements'][1]['selector'])
    register_button = driver.find_element(By.XPATH, ui_context['ui_elements'][2]['selector'])

    username_field.send_keys(username)
    password_field.send_keys(password)
    register_button.click()
    time.sleep(2) #Allow time for page update
    
    # Placeholder for assertion.  Replace with actual assertion based on your application's feedback mechanism.
    #  This might involve checking for success message, error message, or other UI changes.
    assert expected in driver.page_source, f"Expected '{expected}', but got '{driver.page_source}'"


for test_case in ui_context['test_cases']:
    register(test_case['username'], test_case['password'], test_case['expected'])


driver.quit()
