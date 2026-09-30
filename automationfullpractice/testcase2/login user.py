from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

# Verify home page
assert "Automation Exercise" in driver.title
print("Home page visible successfully")

# Click on 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# Verify 'Login to your account'
assert "Login to your account" in driver.page_source
print("Login to your account is visible")

# Enter email + password (replace with dynamic email if needed)
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("malikaaaa@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Password123")

# Click 'Login'
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

# Wait until "Logged in as Malika" is visible
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
    )
    print("Login successful")
except:
    print("Login confirmation not visible! Handling possible ad overlay...")
    try:
        # Handle ad overlay if it appears
        driver.switch_to.frame("aswift_0")
        driver.switch_to.frame("ad_iframe")
        driver.find_element(By.XPATH, "//div[@id='dismiss-button']").click()
        driver.switch_to.default_content()
        # Try waiting again for the login confirmation
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
        )
        print("Login successful after closing ad")
    except:
        print("Ad not present or login confirmation still not visible")

# Click 'Delete Account'
delete_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))
)
delete_btn.click()

# Verify 'ACCOUNT DELETED!'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account Deleted!')]"))
)
print("Account deleted successfully")

# Click 'Continue' after delete
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))
).click()

driver.quit()
