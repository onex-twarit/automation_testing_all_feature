Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on click on new sms, click on quick sms
    And select campaign for ICICIAdmin
    And select sender ID
    And add recipients for iciciadmin
    And insert short template, select filter as dropdown
    And click on send, then send now
    And click on New SMS

    And go to reports
    And click on MIS tab
    And click on total counts and click on search
    And click on view details with TUC name 'ICICIAdmin'
    And store mobile number, uuid, sender ID for ICICIAdmin
    And go to search tab select ICICIAdmin TUC
    And select filter as mobile
    And click on search
    And verify the data
    And select filter as UUID
    And click on search
    And verify the data
    And select filter as sender ID with mobile
    And click on search
    And verify the data

    And Close driver window