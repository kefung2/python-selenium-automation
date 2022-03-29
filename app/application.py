from page.hw7 import HW7
from page.hw8_page import HW8
from page.open_page import open_page

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.hw7 = HW7(self.driver)
        self.hw8 = HW8(self.driver)
        self.open = open_page(self.driver)