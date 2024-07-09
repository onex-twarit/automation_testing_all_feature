Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button


    And go to Routing Reports
    And go to Gateway Details tab
    And select the GW id 207 from dropdown
    And click on search
    And click on Bulk Change Gateway
    And on warning window pop-up click proceed
    And select the selected and select gateways from the dropdown
    And click on proceed
    And click on final proceed then ok

    And go to User Management
    And go to TUC tab
    And click on search TUC
    And click on ICICIAdmin TUC edit
    And all the selected GW ID should be 208
    And click on update


    And Close driver window
