Feature: logout
  Scenario: logout from the user home page
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see the logout button "Delogare Cristian"
    When I press logout button
    Then I should be on the website home page