Feature: infoupdate

  @full_update
  Scenario: update personal informations with valid data
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

  @invalid_phone_number
  Scenario Outline: update phone number field with letters or simbols
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see the logout button "Delogare Cristian"
    When I press info button "Informatii cont"
    Then I should be on the info page
    When I enter a "<letters_or_simbols>" on "Telefon" field
    And I press save button "Salveaza"
    Then The new phone number:"<letters_or_simbols>" should not be saved

    Examples:
      | letters_or_simbols |
      | aLa                |
      | @#$%               |
   #   | aA#$%^!            |


  @sectors
  Scenario: verify if sectors appear on city list when value "Bucuresti" is
  selected on  county list
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see the logout button "Delogare Cristian"
    When I press info button "Informatii cont"
    Then I should be on the info page
    When I select "Bucuresti" option from "Judet/Sector" hidden list
    Then I should see Sector 1 to 6 on the "Oras" hidden list

    @empty_fields
    Scenario: verify if an error message appear when i try to let the name and surname
      fields empty on the infoupdate page
      Given I am on the login page
      When I enter a valid email
      And I enter a valid password
      And I press login button "Autentificare"
      Then I should be on the user home page
      And I should see the logout button "Delogare Cristian"
      When I press info button "Informatii cont"
      Then I should be on the info page
      When I let the "Prenume" field empty
      And I let the "Nume" field empty
      And I press save button "Salveaza"
      Then I shoud see an error message


  @change_email
  Scenario: verify if i could change email address
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I press login button "Autentificare"
    Then I should be on the user home page
    And I should see the logout button "Delogare Cristian"
    When I press info button "Informatii cont"
    Then I should be on the info page
    When I try to change the email address
    Then I should not to be able to change it

