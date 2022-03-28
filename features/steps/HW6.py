from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

privacy_link = (By.CSS_SELECTOR, "p a[href*='privacy']")

@given('Open Amazon T&C page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_orig_win(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(*privacy_link).click()
    context.driver.wait.until(EC.new_window_is_opened)

@when('Switch to the newly opened window')
def switch_to_new_win(context):
    new_window = context.driver.window_handles
    context.driver.switch_to.window(new_window[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window and switch back to original')
def close_new_win_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'))
