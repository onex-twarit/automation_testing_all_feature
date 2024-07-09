# Login to tuc – new sms – quick sms – send sms using recipients and group –
# split schedule – send – verify numbers – verify credits – close.
  Feature: Onextel

  Scenario: Quick SMS using group and recipients

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page tuc
    And go to new sms then to quick sms
    And add recipients and group, uncheck remove dup then check split schedule
    And send it and then verify numbers and credits
    And close the browser
