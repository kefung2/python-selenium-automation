from selenium.webdriver.common.by import By

from page.base_page import Page

class HW7(Page):

    ORDER = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART = (By.ID, "nav-cart-count")
    SIGN_IN_PAGE_ACTUAL_RESULT = (By.XPATH, "//label[@for='ap_email']")
    CART_ISEMPTY_RESULT = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    CART_COUNT = (By.ID, "nav-cart-count")

    def open_home_page(self):
        self.open_page()

    def click_on_order(self):
        self.click(*self.ORDER)

    def verify_sign_in_page_open(self):
        expected_result = 'Email or mobile phone number'
        self.verify_text(expected_result, *self.SIGN_IN_PAGE_ACTUAL_RESULT)

    def click_cart_icon(self):
        self.click(*self.CART)

    def verify_cart_isEmpty(self):
        expected_result = 'Your Amazon Cart is empty'
        self.verify_text(expected_result, *self.CART_ISEMPTY_RESULT)

    ###################################################
    # Add item to cart

    def search_for_item(self, keyword):
       self.input_text_with_key(keyword, *self.SEARCH_BOX)

    def click_on_item(self):
        self.click(*self.PRICE)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def verify_cart(self, num):
        self.verify_text(num, *self.CART_COUNT)