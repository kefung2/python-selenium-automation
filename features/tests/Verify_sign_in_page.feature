# Created by kevin at 2/9/2022
Feature: Logged out user get send to sign up page when click on sign-in function
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Orders
    Then Send to Sign in Page