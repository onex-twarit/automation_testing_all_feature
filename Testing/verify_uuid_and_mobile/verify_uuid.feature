Feature: Verify UUID

  Scenario: Verify UUID

    Given Launch the browser
    Then open login page
    And Enter user name and password for TUC
    And open dashboard page, go to NEW SMS, then quick english SMS
    And Select campaign name as 'uuid and mobile check', then sender ID
    And add number in recipients, then select template, click on select
    And click on send button, then click on send now button
    And on new window click on New SMS button
    And verify the credits on the same window
    And go to reports, in MIS tab click on the day/time, click on search
    And find the latest entry and click under the action
    And take the mobile num and log out TUC
    And Enter user name and password for SA
    And open dashboard page, go to Report, go to search tab
    And enter the mobile number in the field, click on search
    And verify the details
    And close