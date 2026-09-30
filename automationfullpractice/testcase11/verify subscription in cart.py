from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1 & 2. Launch browser and navigate to URL
driver.get("http://automationexercise.com")
time.sleep(2)

# 3. Verify home page is visible successfully
print("Home Page Visible:", "Automation Exercise" in driver.title)

# 4. Click 'Cart' button
driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
time.sleep(2)

# 5. Scroll down to footer
footer = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", footer)
time.sleep(2)

# 6. Verify text 'SUBSCRIPTION'
subscription = driver.find_element(By.XPATH, "//h2[text()='Subscription']")
print("SUBSCRIPTION Visible:", subscription.is_displayed())

# 7. Enter email address and click arrow button
driver.find_element(By.ID, "susbscribe_email").send_keys("test@gmail.com")
driver.find_element(By.ID, "subscribe").click()
time.sleep(2)

# 8. Verify success message is visible
success_msg = driver.find_element(By.XPATH, "//*[contains(text(),'You have been successfully subscribed!')]")
print("Success Message Visible:", success_msg.is_displayed())

driver.quit()
