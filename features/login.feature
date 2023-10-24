#In fisierul feature sunt create scenarile de testare impreuna cu pasii de urmat folosind limbajul Gherkin.
# Am implementat 4 scenarii de testare: 3 de testare negativa si unul de testare pozitiva.

#Apelare in Terminal: behave **/features/login.feature

Feature: login

 @invalid_credentials
  Scenario: login with invalid credentials
    Given I am on the login page
    When I enter an invalid email
    And I enter an invalid password
    And I press login button "Autentificare"
    Then I should see an error message

 @invalid_email
  Scenario: login with invalid email and valid password
    Given I am on the login page
    When I enter an invalid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should see an error message

 @invalid_password
  Scenario: login with valid email and invalid password
    Given I am on the login page
    When I enter a valid email
    And I enter an invalid password
    And I press login button "Autentificare"
    Then I should see an error message

  @valid_credentials
  Scenario: login with valid credentials
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see "Bun venit, Cristian!"
    And I should see the logout button "Delogare Cristian"

