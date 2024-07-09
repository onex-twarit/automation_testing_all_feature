Feature: Campaign SMS with file and group Schedule

  Scenario: file and group Schedule with campaign sms
    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page
    And click on new sms, click on campaign sms
    And upload file
    And add campaign 'campaign file group schedule', fill the present fields, click on Add
    And add group
    And insert template
    And check schedule sms
    And click on schedule, then on schedule now button
    And click on New SMS
    And go to Reports, go to MIS tab, click on total counts
    And search with campaign name 'campaign file group schedule'
    And verify with name 'campaign file group schedule'
    And go to summary tab check all and web(with group and file)
    And go to scheduled campaign, verify 'campaign file group schedule' name
    And delete schedule
    And close