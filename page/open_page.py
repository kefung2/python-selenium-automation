from selenium.webdriver.common.by import By

from page.base_page import Page

class open_page(Page):

    def open_main(self):
        self.open_page()

    def open_sub(self, link):
        self.open_page(link)