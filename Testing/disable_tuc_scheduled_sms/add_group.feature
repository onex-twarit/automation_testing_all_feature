Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "SBIUser" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click phonebook
    And click groups tab
    And click add group button
    And add group name and description
    And click on add button

    And click contacts tab
    And click add contacts button
    And choose upload bulk contact
    And select group for the uploaded file
    And click on add button

    And Close driver window
