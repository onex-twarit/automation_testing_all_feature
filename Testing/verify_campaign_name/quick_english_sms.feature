Feature: Verify campaign name

  Scenario: Verify campaign name with quick english sms

    Given Launch the browser
    Then open login page
    And Enter user name and password for TUC
    And open dashboard page, go to NEW SMS, then quick english SMS
    And in Campaign name, click on add icon for new campaign
    And on new window, fill the present fields, click on Add
    And add number in recipients, then select template, click on select
    And click on send button, then click on send now button
    And on new window click on New SMS button
    And verify the credits on the same window
    And go to reports, in MIS tab click on the day/time, click on search
    And find the latest entry and click under the action
    And check uuid and status
    And close