Feature: In 'ALL' option search field should be removed

  Scenario: TUC (DLT > Template)

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page tuc
    And go to DLT then to template tab
    And select ALL from the search type dropdown
    And click on search
    And close the browser
