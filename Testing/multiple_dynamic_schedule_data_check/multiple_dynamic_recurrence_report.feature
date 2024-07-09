Feature: Multiple Dynamic SMS with Split Schedule

    Scenario: Split Schedule with multiple dynamic sms
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on multiple dynamic sms
        And upload file
        And add campaign 'multiple dynamic recurrence', fill the present fields, click on Add
        And select column for recipients and template content
        And check recurrence box
        And click on schedule, then on schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab, click on total counts
        And search with campaign name 'multiple dynamic recurrence'
        And verify with name 'multiple dynamic recurrence'
        And go to summary tab check all and web
        And go to scheduled campaign, verify 'multiple dynamic recurrence' name
        And delete schedule
        And close