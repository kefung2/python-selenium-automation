# Created by kevin at 3/28/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Using a dropdown and search for an item in a different Amazon department.
    Given Open Amazon page
    When Select Apps & Games
    And Look for kirby in department
    Then Verify search result is in Apps & Games


  Scenario: Verify Use can see new arrival deal
    Given Open Amazon page gp/product/B074TBCSC8
    Then Verify user see the deal