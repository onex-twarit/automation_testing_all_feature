Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on credits
    And click on update credit button
    And fill the present fields
    And click on update

    And Close driver window
