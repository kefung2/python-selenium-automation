from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_page(context):
    context.app.hw7.open_home_page()

@given('Open Amazon page {target}')
def open_amazon(context, target):
    context.driver.get(target)
    sleep(1)

@when('Click Amazon Orders link')
def click_order(context):
    context.app.hw7.click_on_order()
    sleep(1)

@then('Verify Sign In page is opened')
def verify_landing_page(context):
    context.app.hw7.verify_sign_in_page_open()
