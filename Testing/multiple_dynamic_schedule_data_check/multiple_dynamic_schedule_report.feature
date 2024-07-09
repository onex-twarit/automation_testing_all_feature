Feature: Multiple Dynamic SMS with Schedule

    Scenario: Schedule with multiple dynamic sms
        Given Launch the browser
        Then open login page
        And Enter user name and password for tuc
        And open dashboard page
        And click on new sms, click on multiple dynamic sms
        And upload file
        And add campaign 'multiple dynamic schedule', fill the present fields, click on Add
        And select column for recipients and template content
        And check schedule box
        And click on schedule, then on schedule now button
        And click on New SMS
        And go to Reports, go to MIS tab, click on total counts
        And search with campaign name 'multiple dynamic schedule'
        And verify with name 'multiple dynamic schedule'
        And go to summary tab check all and web
        And go to scheduled campaign, verify 'multiple dynamic schedule' name
        And delete schedule
        And close