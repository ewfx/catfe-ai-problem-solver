from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:4200')
        self.ui_context = {
            'module': 'login.component',
            'ui_elements': [
                {'name': 'username_field', 'selector': "//*[@id='username']", 'type': 'input', 'placeholder': 'Enter your username', 'required': True},
                {'name': 'password_field', 'selector': "//*[@id='password']", 'type': 'input', 'placeholder': 'Enter your password', 'required': True},
                {'name': 'sign_in_button', 'selector': "//button[@type='submit']", 'type': 'button', 'text': 'Sign In'}
            ],
            'test_cases': [
                {'scenario': 'Valid Registration', 'username': 'user', 'password': 'password', 'expected': 'Registration successful'},
                {'scenario': 'Invalid Registration - Missing Username', 'username': '', 'password': 'password', 'expected': 'Username is required'},
                {'scenario': 'Invalid Registration - Missing Password', 'username': 'user', 'password': '', 'expected': 'Password is required'}
            ]
        }

    def test_login(self):
        for case in self.ui_context['test_cases']:
            username_field = self.driver.find_element(By.XPATH, self.ui_context['ui_elements'][0]['selector'])
            password_field = self.driver.find_element(By.XPATH, self.ui_context['ui_elements'][1]['selector'])
            sign_in_button = self.driver.find_element(By.XPATH, self.ui_context['ui_elements'][2]['selector'])

            username_field.clear()
            username_field.send_keys(case['username'])
            password_field.clear()
            password_field.send_keys(case['password'])
            sign_in_button.click()

            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + case['expected'] + "')]")))
                print(f"{case['scenario']} passed")
            except:
                print(f"{case['scenario']} failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
