from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

SEARCH_BAR = (By.ID, "helpsearch")
CART = (By.ID, "nav-cart-count")

@given('Open Amazon Support page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    sleep(1)

@when('Input {key_word} into search bar')
def click_order(context, key_word):
    search = context.driver.find_element(*SEARCH_BAR)
    search.clear()
    search.send_keys(key_word)
    sleep(1)

@when('Press Enter')
def press_enter(context):
    context.driver.find_element(*SEARCH_BAR).send_keys(Keys.RETURN)

@then('Result for {key_word} are shown')
def verify_landing_page(context, key_word):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text

    print("Test Success" if actual_result == expected_result else "Test Fail")

    assert expected_result == actual_result, "Expected Result and Actual Result Don't Match"


@when("Click on Cart Icon")
def click_on_cart_icon(context):
    cart = context.driver.find_element(*CART).click()

@then("Verifies Cart is Empty")
def empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty").text

    print("Test Success" if actual_result == expected_result else "Test Fail")

    assert expected_result == actual_result, "Expected Result and Actual Result Don't Match"
