Feature: User login into Nory

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Application run test
    Given the user navigate to the URL
    Then verify the title of the page

  Scenario: Login test with valid user
    Given the user navigate to the URL
    When the user enter the credentials for valid user
    Then user should able to login successfully

  Scenario: Logout functionality test
    Given the user navigate to the URL
    When the user enter the credentials for valid user
    Then user should able to login successfully
    Then user click on logout button
    Then user should be able to logout successfully


  Scenario: Reset functionality test
    Given the user navigate to the URL
    When user click on forgot password link
    Then user enter the email address to reset the password
    Then user click on reset button
    Then Email should be sent to user