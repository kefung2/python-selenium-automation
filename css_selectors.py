from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# by ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# by tag and ID
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
# by class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us')
# by multiple classes
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')
# by attribute
driver.find_element(By.CSS_SELECTOR, "[href='/ref=nav_logo']")
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=nav_logo']")
# partial attr
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")
# travelling through nodes
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_signin_notification_privacy_notice']")
# from parent to child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_privacy_notice')]")
# from child to parent, only with XPath
driver.find_element(By.XPATH, "//div[./a[contains(@href, 'ap_signin_notification_privacy_notice')]]")


