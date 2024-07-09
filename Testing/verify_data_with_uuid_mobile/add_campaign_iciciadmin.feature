Feature: Login

  Scenario: Login child tuc sales
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And click campaign
    And click on add campaign button
    And add campaign name iciciadmin, then click on add

    And Close driver window

