Feature: Quick SMS with recipients and group split schedule

    Scenario: Split Schedule
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on click on new sms, click on quick sms
        And add campaign 'quick split schedule', fill the present fields, click on Add
        And then add sender ID, add recipients and group, insert template
        And check schedule sms for 1 hour
        And click on schedule, then on schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab
        And verify with name 'quick split schedule'
        And go to summary tab check all and web(recipients and group)
        And go to scheduled campaign, verify 'quick split schedule' name
        And delete schedule
        And close