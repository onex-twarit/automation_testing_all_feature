Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on credits
    And click on update credit button
    And select sales tuc with 50000 credits
    And click on update

    And log out ICICIAdmin

    And Enter Username "sales" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on credits
    And click on update credit button
    And select loanuser tuc with 25000 credits
    And click on update

    And Close driver window

