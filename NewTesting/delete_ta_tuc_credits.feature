Feature: Login users and delete credits TA/TUC

  Scenario: Login SuperAdmin
    Given navigate to the login page at "url"
    When enter username "sausername" and password "sapassworddefault"
    And click the login button
    And either dashboard page or change password page should appear "sapassworddefault","sapasswordnew"
    And Click on User Management
    And click on show tenant
    And click on onexadmin credits button and delete 100000 credits and ta
    And go to users tab ta and click on search
    And delete user tenant1admin12

  Scenario: Login TenantAdmin
    Given navigate to the login page at "url"
    When Enter Tenant Username "ta_username" and password "ta_password"
    And Click the login button
    And In TA either dashboard page or change password page should appear "ta_pass","ta_new_password"
    And go to User Management page
    And go to TUC tab
    And click on newtuc credits button and delete 5000 credits and tuc
    And go to users tab tuc and click on search
    And delete user newTucUser