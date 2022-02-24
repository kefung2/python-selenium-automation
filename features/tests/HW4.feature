# Created by kevin at 2/23/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Open amazon BestSellers page and verify there are 5 links
    Given Open Amazon page https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
    Then Verify there are 5 item


  Scenario: # Add any product into the cart, and make sure it’s there
    Given Open Amazon page https://www.amazon.com/
    When Search for LEGO
    And Click on item
    And Add to cart
    Then Verifies Cart has 1 item