from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART = (By.ID, "add-to-cart-button")
BEST_SELLER_LINKS = (By.XPATH, "//a[contains(@href, '/ref=zg_bs_tab')]")

@when('Search for {item}')
def search_for(context, item):
    context.app.hw7.search_for_item(item)

@when('Click on item')
def click_on_item(context):
    context.app.hw7.click_on_item()

@when('Add to cart')
def add_to_cart(context):
    context.app.hw7.add_to_cart()

@then('Verifies Cart has {num} item')
def verifiy_cart_has_item(context, num):

    context.app.hw7.verify_cart(num)

@then('Verify there are {x} item')
def verify_num_of_element(context, x):
    expected_result = int(x)
    actual_result = len(context.driver.find_elements(*BEST_SELLER_LINKS))

    print(actual_result)
    print("Test Success" if actual_result == expected_result else "Test Fail")

    assert expected_result == actual_result, "Expected Result and Actual Result Don't Match"