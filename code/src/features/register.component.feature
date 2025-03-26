```gherkin
Feature: User Registration

  Scenario Outline: Verify registration functionality with different inputs
    Given I am on the registration page
    When I enter "<username>" in the username field
    And I enter "<password>" in the password field
    And I click on the Register button
    Then I should see "<expected>" message

    Examples:
      | scenario                     | username    | password       | expected                     |
      | Valid Registration           | validuser   | validpassword   | Registration successful       |
      | Invalid Registration - Missing Username | ""          | validpassword   | Username is required         |
      | Invalid Registration - Missing Password | validuser   | ""             | Password is required         |


```

This feature file leverages the Scenario Outline to efficiently test multiple scenarios with varying inputs.  The examples table clearly defines the test data for each scenario, making the feature file concise and readable.  The step definitions (not included here, as they are implementation specific) would interact with the UI using the selectors provided in the context.  For instance, a step definition for "I enter "<username>" in the username field" would likely use the selector `//*[@id='username']` to locate the username field and enter the provided username.  Error handling and specific error message verification would also be implemented within the step definitions.
