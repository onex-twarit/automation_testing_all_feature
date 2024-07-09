Feature: Onextel tuc login

  Scenario: Recurrence with group

    Given Launch the browser tuc
    Then open login page tuc
    And Enter user name and password tuc
    And open dashboard page tuc
    And go to NEW SMS then to quick unicode with group
    And present fields to be filled with group
    And check on recurrence, unicode, multipart and click on send
    And on new window click on proceed, before that verify the labels
    And check if message is sent successfully
    And close the browser after sending
