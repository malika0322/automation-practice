from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1 & 2. Launch browser and open URL
driver.get("http://automationexercise.com")
time.sleep(2)

# 3. Verify home page is visible
print("Home Page Visible:", "Automation Exercise" in driver.title)

# 4. Scroll down to footer
footer = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", footer)
time.sleep(2)

# 5. Verify text 'SUBSCRIPTION'
subscription_text = driver.find_element(By.XPATH, "//h2[text()='Subscription']")
print("SUBSCRIPTION Text Visible:", subscription_text.is_displayed())

# 6. Enter email and click arrow button
driver.find_element(By.ID, "susbscribe_email").send_keys("testemail@gmail.com")
driver.find_element(By.ID, "subscribe").click()
time.sleep(2)

# 7. Verify success message
success_msg = driver.find_element(By.XPATH, "//*[contains(text(),'You have been successfully subscribed!')]")
print("Success Message Visible:", success_msg.is_displayed())

driver.quit()
