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

# 4. Click 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# 5. Verify 'New User Signup!'
assert "New User Signup!" in driver.page_source
print("New User Signup! is visible")

# 6. Enter name and already registered email
driver.find_element(By.NAME, "name").send_keys("Malika")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("malikaaaa@gmail.com")

# 7. Click 'Signup'
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()

# 8. Verify error 'Email Address already exist!'
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Email Address already exist!')]"))
)
print("Error 'Email Address already exist!' is visible")

driver.quit()
