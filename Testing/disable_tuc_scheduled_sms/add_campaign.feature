Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "SBIUser" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click campaign
    And click on add campaign button
    And add campaign name, then click on add

    And Close driver window
