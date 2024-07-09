Feature: Unicode SMS with recipients and group Split Schedule

    Scenario: Split Schedule
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on unicode sms
        And add campaign 'unicode recurrence', fill the present fields, click on Add
        And then add sender ID, add recipients and group, insert template
        And check allow multi part and allow unicode
        And check recurrence for 1 hour
        And click on schedule, then on schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab
        And verify with name 'unicode recurrence'
        And go to summary tab check all and web(recipients and group)
        And go to scheduled campaign, verify 'unicode recurrence' name
        And delete schedule
        And close