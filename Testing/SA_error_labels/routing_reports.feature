Feature: Error labels in SA

  Scenario: SA > Routing Reports
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Routing Reports
    And go to TUC Details tab, 'TUC doesn't exists' error label should come
    And go to gateway details tab, click on search
    And error label should come for SMPPC and TUC using gateway
    And close

