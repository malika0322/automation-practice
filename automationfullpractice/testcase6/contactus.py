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

# 4. Click 'Contact Us'
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a').click()

# 5. Verify 'GET IN TOUCH'
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/h2'))
)
print("'GET IN TOUCH' is visible")

# 6. Enter details
driver.find_element(By.NAME, "name").send_keys("Malika")
driver.find_element(By.NAME, "email").send_keys("malikaaaa@gmail.com")
driver.find_element(By.NAME, "subject").send_keys("Test Subject")
driver.find_element(By.NAME, "message").send_keys("This is a test message.")

# 7. Upload file
driver.find_element(By.NAME, "upload_file").send_keys(r"C:\Users\acer\Downloads\dam.txt")  # change path

# 8. Click 'Submit'
submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "submit"))
)
submit_btn.click()


# 9. Handle alert
WebDriverWait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

# 10. Verify success message
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Success! Your details have been submitted successfully.')]"))
)
print("Success message is visible")

# 11. Click 'Home' and verify home page
driver.find_element(By.LINK_TEXT, "Home").click()
assert "Automation Exercise" in driver.title
print("Landed on home page successfully")

driver.quit()
