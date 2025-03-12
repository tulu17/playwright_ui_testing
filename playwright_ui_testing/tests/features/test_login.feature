Feature: Login Functionality


    Scenario: Positive login case with correct credentials
      Given the login page is launched
      When the user types "student" username into the username field
      And the user types "Password123" password into the password field
      And the user pushes submit button
      Then the new page url should contain "practicetestautomation.com/logged-in-successfully/" text
      And the new page should contain "successfully logged in" text
      And the "Log out" button should be displayed on the new page


    Scenario: Negative login case with correct user and wrong password
      Given the login page is launched
      When the user types "studen" username into the username field
      And the user types "Password123" password into the password field
      And the user pushes submit button
      Then the error message should be displayed
      And the error message text "Your username is invalid!" should be displayed


    Scenario: Negative login case with incorrect user and correct password
      Given the login page is launched
      When the user types "student" username into the username field
      And the user types "Password12" password into the password field
      And the user pushes submit button
      Then the error message should be displayed
      And the error message text "Your password is invalid!" should be displayed