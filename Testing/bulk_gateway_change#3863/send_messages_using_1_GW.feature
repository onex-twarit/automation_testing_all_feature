Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to New SMS
    And go to quick english SMS
    And add campaign with 'bulk_GW_camp_two'
    And select Sender ID 'ONEXTL'
    And add group test(22)
    And insert template English Short
    And click on send
    And store the total credit counts
    And on SMS confirmation window click on send now
    And click on new sms
    And verify the deducted credits

    And go to Reports TUC
    And go to MIS tab, click on total counts
    And click on search
    And find campaign bulk_GW_camp_two and click on view details
    And match the total deducted credits with submitted credits

    And log out TUC
    And Enter Username "onexsa" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to report SA
    And go to search tab
    And enter uuid for GW 208 and click on search

    And Close driver window