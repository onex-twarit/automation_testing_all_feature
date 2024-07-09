Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button
    And open dashboard

    And click on All Schedule
    And click on view all schedule
    And verify present tuc search field
    And verify limit box
    And verify search button
    And verify delete all button

    And Close driver window
