# Created by kevin at 2/17/2022
Feature: # HW3
  # Enter feature description here

  Scenario: # Update a test case for support search using BDD
    Given Open Amazon Support page
    When Input cancel order into search bar
    And Press Enter
    Then Result for cancel order are shown

  Scenario: # Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.
    Given Open Amazon page https://www.amazon.com/
    When Click on Cart Icon
    Then Verifies Cart is Empty