Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button
# -----------------------------------------------------------------------------
    And go to NEW SMS then to quick english sms
#    And add recipients
#    And present fields to be filled
    And check on schedule sms, split into campaigns and click on send
#    And new window for confirmation
#    And again on new window click on proceed
#    And check if message is sent
# -----------------------------------------------------------------------------
    And Close driver window