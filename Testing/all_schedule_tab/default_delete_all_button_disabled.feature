Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button
    And open dashboard

    And click on All Schedule
    And click on view all schedule
    And verify present delete all button is disabled
    And verify its enabled after clicking on search button with records


    And Close driver window
