from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# init driver
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)
driver.maximize_window()


# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, "helpsearch")

search.clear()
search.send_keys('cancel order')
search.send_keys(Keys.RETURN)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
print(actual_result)

# verify
assert expected_result == actual_result, "test fail"
driver.quit()