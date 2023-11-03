# BDD Testing: QuickMobile.ro
***Quickmobile.ro** is a website that exclusively sells electronic products from over 150 IT&C brands, both in Romania and across Europe through its online store.*

Automated testing represents a dynamic and analytical testing of software products, involving the use of a program to execute test procedures (test cases) or complete test scenarios. Its purpose is to run repetitive or customizable tests for a wide variety of applications with minimal human intervention. The advantages of such testing include efficiency, precision, reusability, and scalability.

In this project, the Python programming language was used, with the PyCharm Integrated Development Environment (IDE), along with the Selenium and Behave libraries.

PyCharm is an IDE developed by JetBrains, the company behind IntelliJ IDEA, to provide a simple yet powerful IDE to make coding easier for developers using Python as their programming language.

Python is a dynamic, high-level programming language emphasizing code expressiveness and ease of understanding. The language supports multiple programming paradigms, especially imperative (C) and object-oriented (Java) paradigms.

The Selenium library is an open-source suite of tools and libraries used for browser automation. Selenium allows users to test the functionality of websites on various browsers.

The methodology used in this project is Behavior-Driven Development (BDD), which is why the Behave library was utilized. BDD is a software development process derived from Test-Driven Development (TDD) with a greater focus on testing scenarios. BDD activities are similar to TDD, but they have the advantage of adding business scenario descriptions in a language understandable to non-technical users. These descriptions are called feature files and are the first files created in the BDD process, with everything else created to validate the tests described in these feature files.

Gherkin is a descriptive language used in the BDD process to implement business scenarios in a natural language, written in simple English so all involved individuals can understand it.

The design pattern used is the Page Object Model (POM), a design used by the BDD methodology. This design was implemented to group all elements on a web page into a single Python file, so each web page corresponds to a single Python file containing all the elements on that web page and the actions that can be performed on it.

# Project Structure.

The project tests the functionalities of login, logout, and personal data modification in the "My Account" -> "Account Information" section of the website https://www.quickmobile.ro.

In the project preparation, a requirements file was created, containing various libraries/packages/plugins useful for code development. The browser and environment files were created for browser driver instantiation for testing purposes and defining actions to be taken before and after each test. The next step was creating the "features" folder, which contains three feature files (specific to BDD) representing the tested functionalities written as scenarios in the Gherkin language: login.feature, logout.feature, and infoupdate.feature. Additionally, two folders, "pages" and "steps," were created. "pages" contains the logic behind the tests, and "steps" contains the steps for executing tests according to the written scenarios.

Three feature files were defined: infoupdate.feature, login.feature, logout.feature, with the corresponding tested features and scenarios. Tags were used for individual tests in the case of login.feature, allowing for the execution of a single test (@invalid_credentials, @invalid_email, @invalid_password, @valid_credentials). The same approach was taken with infoupdate.feature: @full_update, @invalid_phone_number, @sectors, @empty_fields, @change_email. To test phone numbers, a Scenario Outline was implemented to verify multiple types of invalid phone numbers (letters and symbols).

In the "pages" folder, the base_page file was created to avoid rewriting the same functions/code lines in multiple places, reducing redundant code. All the necessary actions for testing were defined in login_page and info_page, including data, paths, and actions needed to define the test steps for login/logout and updating personal information in the "My Account," "Account Information" section. Both files inherit the BasePage class (created in the base_page file), allowing methods to be called using the "self" parameter. To adhere to the POM design principles, the data, and paths of the tested objects were integrated into the corresponding files, even though it would have been more suitable to define them in a separate file with the relevant classes for code clarity.

In the "steps" folder, two-step definition files were created: infoupdate_steps and login_steps, aiding in the technical implementation of the scenarios described in the feature files. The "context" parameter allows for accessing methods and instantiating objects defined in the "pages" folder.

After the successful execution of all tests, a report was generated for each feature: infoupdate.report.html, login.report.html, and logout.report.html. These reports were generated in the terminal using the "behave" command and can be accessed through a browser thanks to the "-o" parameter.

  # Conclusions. Results.
  
In conclusion, the testing process involved the testing of three functionalities: login, logout, and infoupdate. For the login functionality, four tests were created and executed, initially verifying login with valid credentials, followed by login with invalid credentials. The logout functionality was tested with a single test, verifying that the logout button appears and works after a successful login. All the mentioned tests passed successfully. The final functionality test involved updating personal information in the "My Account," "Account Information" section. The test created for this purpose passed successfully. Four additional aspects of this form were tested:

- Verifying that selecting "Bucharest" from the list of counties results in the display of sector options in the "City" section. Test passed.
- Verifying that the email address used to create the account cannot be modified, as it is set as read-only. Test passed.
- Verifying that leaving the "First Name" and "Last Name" fields empty results in an error message. Test passed.
- Testing whether only digits and not letters or symbols can be used in the phone number field. The test failed, and the first bug was identified. The phone number field should only accept digits. Additionally, a visual bug was identified in the "Account Information" form. In the "County" field, the text used is "County/Sector," but the sector option (when choosing "Bucharest") appears in the immediately following "City" field.

The identified bugs do not have a significant impact on users. During the order placement, users are required to enter a valid phone number, and the visual bug disappears.
