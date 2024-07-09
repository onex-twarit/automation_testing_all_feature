Feature: Dynamic SMS with split schedule

    Scenario: Split Schedule with dynamic sms
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on dynamic sms
        And upload file
        And add campaign 'dynamic split schedule camp', fill the present fields, click on Add
        And insert template
        And check schedule sms, split schedule for 1 hour
        And click on schedule, then on yes, schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab, click on total counts
        And search with campaign name 'dynamic split schedule camp'
        And verify with name 'dynamic split schedule camp'
        And go to summary tab check all and web
        And go to scheduled campaign, verify 'dynamic split schedule camp' name
        And delete schedule
        And close