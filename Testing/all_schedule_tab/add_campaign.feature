Feature: Login in code

  Scenario:  Analytics Tab Login
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ChildOne" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click campaign
    And click on add campaign button
    And add campaign name, then click on add

    And log out child TUC
    And Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click campaign
    And click on add campaign button
    And add campaign name, then click on add

