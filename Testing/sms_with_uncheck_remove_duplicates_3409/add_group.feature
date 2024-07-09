Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

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

