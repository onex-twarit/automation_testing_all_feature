Feature: Adding master Credits to Superadmin and giving few credits to Tenant.

  Scenario: Updation of master credits and adding few credits to tenant.
    Given navigate to the login page at "url"
    And Verify that the URL is working and login page is displayed.
    When enter username "sausername" and password "sapassworddefault"
    And click the login button
    And either dashboard page or change password page should appear "sapassworddefault","sapasswordnew"
    And Verify that the system admin has a left-side menu option “Master Credits” for tenant configuration.
    And The system admin clicked on the Master Credits Menu option and clicked on the “update credits” button.
    And Verify that the update credits window popup
    And The system admin entered "mastercredits" credits and clicked on the add button
    And Verify that "mastercredits" credits were added/updated successfully.
    And The system admin clicked on the Credits Menu option, and clicked on the “update credits” button.
    And Verify that the update credits window for tenants popup
    And system admin selects the newly created "tenant_name",adds the credit radio button,entered credit "tenantcredits",clicked on Update.
    And Verify that "tenantcredits" credits added to the newly created tenant account "tenant_name".
    And "tenantcredits" credits were debited from the system admin’s master credits.
    And Click on logout
    And Verify that the system admin is logged out successfully

  Scenario:Verification of credits to Tenant.
    When enter TA username "user" and password "ta_pass"
    And  click the login button
    And In TA either dashboard page or change password page should appear "ta_pass","ta_new_password"
    And Verify that on the dashboard the tenant admin is able to see "tenantcredits" credits in his account.
