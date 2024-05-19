@web
Feature: Finding the Truth
  As a user,
  I should be able to know in detail about the case against Kevin
  So that I can pass the right verdict

  Background: Launch the case details portal
    Given I go to the Main page to select a case
    And I click the START button

  Scenario: Select Kevin's case
      When I select case of Kevin
      Then I judge the selected case

    Scenario: Check who is to Blame
      When I select who is to blame
      Then I judge the selected case




