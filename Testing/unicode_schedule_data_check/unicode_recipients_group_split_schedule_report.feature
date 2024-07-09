Feature: Unicode SMS with recipients and group Split Schedule

    Scenario: Split Schedule
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on unicode sms
        And add campaign 'unicode split schedule', fill the present fields, click on Add
        And then add sender ID, add recipients and group, insert template
        And check allow multi part and allow unicode
        And check schedule sms, split schedule for 1 hour, split number
        And click on schedule, then on yes, schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab
        And verify with name 'unicode split schedule'
        And go to summary tab check all and web(recipients and group)
        And go to scheduled campaign, verify 'unicode split schedule' name
        And delete schedule(recipients and group)
        And close