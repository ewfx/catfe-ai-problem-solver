```gherkin
Feature: Login Functionality

  Background:
    Given I am on the login page

  Scenario Outline: User login validation
    When I enter username "<username>"
    And I enter password "<password>"
    And I click on the Sign In button
    Then I should see "<expected>"

    Examples:
      | scenario                     | username   | password       | expected                     |
      | Valid Registration           | validuser | validpassword | Registration successful       |
      | Invalid Registration - Missing Username |  | validpassword | Username is required          |
      | Invalid Registration - Missing Password | validuser   |              | Password is required         |


```

**Supporting Code Considerations (Not part of the Feature File but crucial):**

To make this Cucumber feature file executable, you'll need supporting code in a language like Java, Python, or Ruby. This code would:

1. **Page Object Model (POM):**  Create a `LoginPage` class (or similar) to encapsulate the UI elements defined in the context. This class would use the selectors provided (`//*[@id='username']`, etc.) to interact with the page. Example (Python with Selenium):

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_field = (By.XPATH, "//*[@id='username']")
    password_field = (By.XPATH, "//*[@id='password']")
    sign_in_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()

    def get_error_message(self): # Example for error message retrieval
        # Implement logic to get the error message from the UI
        # This will vary based on your application's design
        return self.driver.find_element(By.ID, "error-message").text # Example selector

```


2. **Step Definitions:**  Write step definitions (using the `Given`, `When`, `Then` keywords) that map the Gherkin steps to the actions performed by the `LoginPage` class.  Example (Python with behave):

```python
from behave import *
from pages.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.driver.get("your_login_page_url")  # Replace with your URL
    context.login_page = LoginPage(context.driver)

@when('I enter username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('I enter password "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('I click on the Sign In button')
def step_impl(context):
    context.login_page.click_sign_in()

@then('I should see "{expected}"')
def step_impl(context, expected):
    message = context.login_page.get_error_message() # Or another method to check success/failure
    assert expected in message, f"Expected '{expected}', but got '{message}'"

```

Remember to adapt the selectors, error message retrieval logic, and the framework (behave, pytest-bdd, etc.) to match your specific project setup.  This expanded answer provides a more complete picture of what's needed for a working automated test.
