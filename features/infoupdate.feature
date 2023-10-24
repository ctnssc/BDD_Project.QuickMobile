Feature: infoupdate
  Scenario: update personal informations
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see the logout button "Delogare Cristian"
    When I press info button "Informatii cont"
    Then I should be on the info page
    When I enter text on "Prenume" field
    And I enter text on  "Nume" field
    And I enter a phone number on "Telefon" field
    And I select an option from "Judet/Sector" hidden list
    And I select an option from "Oras" hidden list
    And I enter text on "Adresa" text box
    And I press save button "Salveaza"
    Then I shoud see my new data saved