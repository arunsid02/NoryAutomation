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