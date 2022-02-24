from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page {target}')
def open_amazon(context, target):
    context.driver.get(target)
    sleep(1)

@when('Click on Orders')
def click_order(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
    sleep(1)

@then('Send to Sign in Page')
def verify_landing_page(context):
    expected_result = 'Email or mobile phone number'
    actual_result = context.driver.find_element(By.XPATH, "//label[@for='ap_email']").text

    assert expected_result == actual_result, "test fail"
