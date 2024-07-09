Feature: Onextel login

# Login to tuc – new sms – quick sms – send sms using recipients – split schedule
# – send – verify numbers – verify credits – click on view schedule – verify record is added or not – close.

  Scenario: Verify record added or not

    Given Launch browser
    Then open the login page
    And Enter the user name and password
    And Dash board page
    And go to NEW SMS then to the quick english sms tuc
    And add recipients and fill the present fields
    And check on split schedule then send it
    And click on view schedule and verify (record added)
    And close browser

#  xpath = '//*[@id="id_3501"]'
#  fullxpath = '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[1]'
