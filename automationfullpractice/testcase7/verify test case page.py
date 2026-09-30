from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("http://automationexercise.com")
driver.maximize_window()

# Verify home page is visible
if "Automation Exercise" in driver.title:
    print("✅ Home page is visible")
else:
    print("❌ Home page not visible")

# Click on 'Test Cases' button
driver.find_element(By.XPATH, "//a[normalize-space()='Test Cases']").click()
time.sleep(2)

# Verify user is navigated to test cases page
if "Test Cases" in driver.title:
    print("✅ Navigated to Test Cases page successfully")
else:
    print("❌ Navigation failed")

# Close browser
driver.quit()
