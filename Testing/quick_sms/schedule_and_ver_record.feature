#Login to tuc – new sms – quick sms – recipients and group – split schedule –send –
#verify numbers – verify credits – click on view schedule – verify record is added or not – close.
Feature: Onextel tuc login

  Scenario: Quick SMS and verify record added or not

     Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page tuc
    And go to new sms then to quick sms
    And add recipients, group and select template
    And check on split schedule, send it
    And verify credits, go to view schedule
    And verify weather record is added or not
    And browser closed