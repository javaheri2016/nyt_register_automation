Feature: Test Plan for The New York Times Login and Registration


  Scenario: Successful login to NYT
    When I go to NYT login page
    And I provide my registered email
    And I provide my registered password
    And I click on login button
    Then I verify account settings dropdown

  Scenario: Try to register with too short password
    When I go to NYT registration page
    And I provide my email
    And I provide my too short password
    And I click on create account button
    Then I verify an error message