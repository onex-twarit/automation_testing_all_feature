Feature: Campaign SMS with group split Schedule

  Scenario: group split Schedule with campaign sms
    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page
    And click on new sms, click on campaign sms
    And add campaign 'campaign group split schedule', fill the present fields, click on Add
    And add group
    And insert template
    And check schedule sms, split schedule
    And click on schedule, then on yes, schedule now button
    And click on New SMS
    And go to Reports, go to MIS tab, click on total counts
    And search with campaign name 'campaign group split schedule'
    And verify with name 'campaign group split schedule'
    And go to summary tab check all and web
    And go to scheduled campaign, verify 'campaign group split schedule' name
    And delete schedule
    And close