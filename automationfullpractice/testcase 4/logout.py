from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

# 6. Enter correct email and password
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("malikaaaa@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Password123")

# 7. Click 'Login' button
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

# 8. Wait until "Logged in as username" is visible
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
)
print("Login successful")

# 9. Click 'Logout' button
logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
)
logout_btn.click()
print("Clicked Logout")

# 10. Verify user is navigated to login page
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login to your account')]"))
)
print("User navigated to login page successfully")

driver.quit()
