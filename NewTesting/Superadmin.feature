Feature: Login functionality of Supeadmin and tenant

  Scenario: create Tenant and its user and verify it.
    Given  navigate to the login page at "url"
    And Verify that the URL is working and login page is displayed.
    When enter username "sausername" and password "sapassworddefault"
    And  click the login button
    And either dashboard page or change password page should appear "sapassworddefault","sapasswordnew"
    And Click on User Management
    And Click on + Add Tenant Button
    And verify Create Tenant web page form is loaded
    And Enter tenant details Name "tenant_name" and "description" and "child_tuc" and "smpps" and "sms_api"
    And Click on Create button
    And Click on Show Tenants Button
    And Verify Tenant "tenant_name" is created successfully


  Scenario: Tenant user creation and logging out.
    And Click on User Management
    And Click on TA User
    And Click on Add User Button
    And Verify that the Create User web page form is loaded
    And Enter tenant User details Name "user", Password "ta_pass", First Name "fname", Last Name "lname", Email "email", Mobile Number "mobileno", Company Name "company", Website "website", Role "userrole",TA"tenant_name"
    And Click on Create user button
    And Click on Search Button in User "user"
    And Verify Tenant user "user" is created successfully
    And Click on logout
    And Verify that the system admin is logged out successfully


  Scenario:Successful login with Tenant credentials.
    When enter TA username "user" and password "ta_pass"
    And  click the login button
    And In TA either dashboard page or change password page should appear "ta_pass","ta_new_password"







