Feature: Unicode SMS with group Recurrence

    Scenario: Recurrence
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on unicode sms
        And add campaign 'recurrence group camp', fill the present fields, click on Add
        And then add sender ID, add group, insert template
        And check allow multi part and allow unicode
        And check recurrence for 1 hour
        And click on schedule, then on schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab
        And verify with name 'recurrence group camp'
        And go to summary tab check all and web
        And go to scheduled campaign, verify 'recurrence group camp' name
        And delete schedule
        And close