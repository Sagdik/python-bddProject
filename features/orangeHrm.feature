Feature: Orange HRM Login function

  Scenario: Login with valid username and password
  Given I launch url on browser
  And  I enter username and password
  When I click on login button
  Then I Should successfully login
