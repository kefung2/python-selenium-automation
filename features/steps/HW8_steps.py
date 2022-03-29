from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@when('Select {department}')
def click_on_department(context, department):
    context.app.hw8.click_on_department(department)

@when('Look for {item} in department')
def search_for_item_in_department(context, item):
    context.app.hw8.search_for_item_in_department(item)

@then('Verify search result is in {department}')
def verify_search_result(context, department):
    context.app.hw8.verify_search_result(department)

@when('Hover New Arrival')
def hover_new_arrival(context):
    context.app.hw8.hover_new_arrival()

@then('Verify user see the deal')
def verofy_user_see_the_deal(context):
    pass