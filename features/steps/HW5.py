from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

Color_selection = (By.CSS_SELECTOR, "#variation_color_name li")
Current_color = (By.CSS_SELECTOR, "#variation_color_name .selection")

@then('Verify all color option')
def verify_all_color_option(context):
    color = context.driver.find_elements(*Color_selection)
    expect_color = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye']

    for i in range(len(color)):
        color[i].click()
        current_color = context.driver.find_element(*Current_color).text
        assert current_color == expect_color[i], f'Actual color is {current_color}, expected {expect_color[i]}'