# Created by kevin at 3/28/2022
Feature: # Rewrite these scenarios with Page Object pattern:
  # Enter feature description here

#amazon_main_steps.py
Scenario: Logged out user sees Sign in page when clicking Orders
   Given Open Amazon page
   When Click Amazon Orders link
   Then Verify Sign In page is opened

#HW3.py
Scenario: 'Your Shopping Cart is empty' shown if no product added
   Given Open Amazon page
   When Click on cart icon
   #Verify 'Your Shopping Cart is empty.' text present
   Then Verifies Cart is Empty

#HW4.py
Scenario: # Add any product into the cart, and make sure it’s there
    Given Open Amazon page
    When Search for LEGO
    And Click on item
    And Add to cart
    Then Verifies Cart has 1 item