
# Logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

# "Create account"
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


# Your name text field
driver.find_element(By.ID, 'ap_customer_name')


# Email text field
driver.find_element(By.ID, 'ap_email')


# Password Text field
driver.find_element(By.ID, 'ap_password')


# password req. text
driver.find_element(By.CSS_SELECTOR, '.auth-inlined-information-message .a-alert-content')


# Re-enter password text field
driver.find_element(By.ID, 'ap_password_check')


# Create you Amazon account button
driver.find_element(By.ID, 'continue')


# Condiditions of Use
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_condition_of_use"]')


# Privacy Notice
driver.find_element(By.CSS_SELECTOR, '[href*="ap_register_notification_privacy_notice"]')


# Sign in
driver.find_element(By.CSS_SELECTOR, "[href*='signin']")

