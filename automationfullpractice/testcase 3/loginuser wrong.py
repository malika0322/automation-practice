from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

# 3. Verify home page
assert "Automation Exercise" in driver.title
print("Home page visible successfully")

# 4. Click on 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# 5. Verify 'Login to your account'
assert "Login to your account" in driver.page_source
print("'Login to your account' is visible")

# 6. Enter incorrect email and password
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("wrongemail@example.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("WrongPassword123")

# 7. Click 'Login' button
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

# 8. Verify error message
try:
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your email or password is incorrect!')]"))
    )
    print("Error message displayed correctly:", error_msg.text)
except:
    print("Error message not found or page did not respond in time")

driver.quit()
