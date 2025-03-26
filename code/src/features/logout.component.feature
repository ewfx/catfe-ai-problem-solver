```gherkin
Feature: Logout Functionality

  Scenario Outline: Successful Logout
    Given I am logged in as "<username>" with password "<password>"
    When I click the logout button
    Then I should be logged out
    And I should see the login page

  Examples:
    | username     | password     |
    | validuser    | validpassword |


  Scenario: Cancel Logout
    Given I am logged in as "validuser" with password "validpassword"
    When I click the logout button
    And I click the cancel button
    Then I should remain logged in
    And I should still see the application's main page


```

**Explanation:**

This Cucumber feature file focuses on the logout functionality, separating successful logout from a cancellation scenario.  It uses scenario outlines to efficiently test logout with various user credentials (though the provided context included registration test cases, which are irrelevant to logout).

* **Feature:** Clearly states the feature being tested.
* **Scenario Outline:**  Allows for running the same scenario with different data sets.  Here, it's used to test logout with different (valid) users.
* **Given:** Sets the pre-conditions.  Assumes a "login" step definition exists.
* **When:** Describes the action performed by the user.
* **Then:** Describes the expected outcome.  Assumes step definitions check for logout and presence of the login/main page.
* **Examples:**  Provides data for the Scenario Outline.
* **Second Scenario:** This handles the cancellation path.


**Note:**  The provided context includes registration test cases which are unrelated to logout.  This feature file only addresses the logout functionality.  A complete test suite would also include separate feature files for registration, login, and potentially other features.  The selectors for the buttons (from the context) are generic and might need adjustments depending on the actual application's HTML structure.  Robust automation would include error handling and more detailed checks beyond simply verifying page presence.
