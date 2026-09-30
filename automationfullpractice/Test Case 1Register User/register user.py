from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Launch browser and 2. Navigate to url
driver.get("http://automationexercise.com")

# 3. Verify home page
if "Automation Exercise" in driver.title:
    print("Home page visible successfully")

# 4. Click on 'Signup / Login'
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# 5. Verify 'New User Signup!'
if "New User Signup!" in driver.page_source:
    print("New User Signup! is visible")

# 6. Enter name and unique email
driver.find_element(By.NAME, "name").send_keys("Malika")
# unique_email="malikaaaa@gmail.com"
unique_email = f"malika{int(time.time())}@example.com"   # unique email each run
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(unique_email)

# 7. Click 'Signup'
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()

# 8. Verify 'ENTER ACCOUNT INFORMATION'
if "ENTER ACCOUNT INFORMATION" in driver.page_source:
    print("ENTER ACCOUNT INFORMATION is visible")

# 9. Fill details
driver.find_element(By.ID, "id_gender2").click()
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "days").send_keys("10")
driver.find_element(By.ID, "months").send_keys("May")
driver.find_element(By.ID, "years").send_keys("2000")

# 10 + 11. Select checkboxes
driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

# 12. Fill details
driver.find_element(By.ID, "first_name").send_keys("Malika")
driver.find_element(By.ID, "last_name").send_keys("Budhathoki")
driver.find_element(By.ID, "company").send_keys("Clothify")
driver.find_element(By.ID, "address1").send_keys("Bhaktapur, Nepal")
driver.find_element(By.ID, "address2").send_keys("Bagmati")
driver.find_element(By.ID, "country").send_keys("Canada")
driver.find_element(By.ID, "state").send_keys("Province")
driver.find_element(By.ID, "city").send_keys("Kathmandu")
driver.find_element(By.ID, "zipcode").send_keys("44600")
driver.find_element(By.ID, "mobile_number").send_keys("9800000000")

# 13. Click 'Create Account'
driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

# 14. Verify 'ACCOUNT CREATED!'
if "Account Created!" in driver.page_source:
    print("Account Created! is visible")

# 15. Wait for and click 'Continue'
continue_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@data-qa='continue-button']"))
)
continue_btn.click()
time.sleep(2)

# 16. Verify 'Logged in as username'
if "Logged in as Malika" in driver.page_source:
    print("Logged in as username is visible")

# 17. Click 'Delete Account'
driver.find_element(By.LINK_TEXT, "Delete Account").click()

# 18. Verify 'ACCOUNT DELETED!'
if "Account Deleted!" in driver.page_source:
    print("Account Deleted! is visible")

driver.find_element(By.LINK_TEXT, "Continue").click()

time.sleep(2)
driver.quit()
