from page.hw7 import HW7

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.hw7 = HW7(self.driver)