Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard

    And click on All Schedule
    And click on view all schedule
    And click on search (with records)
    And check pagination for tuc

    And Close driver window
