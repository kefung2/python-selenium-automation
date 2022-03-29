from page.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class HW8(Page):
    DROPDOWN_MENU = (By.ID, 'searchDropdownBox')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    DEPARTMENT_VERIFY = (By.CSS_SELECTOR, "#filter-n .a-section .a-color-base")
    NEW_ARRIVAL = (By.CSS_SELECTOR, "a[href*='/New-Arrivals']")
    DEAL = (By.CSS_SELECTOR, "a[href*='/s?i=fashion&bbn']")

    def click_on_department(self, department):
        select = Select(self.driver.find_element(*self.DROPDOWN_MENU))
        select.select_by_visible_text(department)

    def search_for_item_in_department(self, item):
        self.input_text_with_key(item, *self.SEARCH_BOX)

    def verify_search_result(self, department):
        self.verify_text(department, *self.DEPARTMENT_VERIFY)

    def hover_new_arrival(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.NEW_ARRIVAL))
        action.perform()

    def verify_user_see_deal(self):
        self.wait_for_element_appear(*self.DEAL)


