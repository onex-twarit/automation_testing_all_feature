#Login to tuc – new sms – quick sms – recipients and group–
#remove duplicate and click on scrub dnd – send – verify numbers – verify credits – close.
Feature: Onextel

  Scenario: Quick SMS(remove dupl) with scrub DND

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page tuc
    And go to new sms then to quick sms
    And add recipients and group remove dup then check scrub dnd, send it
    And on sms confirmation window verify nums and credits
    And close the browser



