from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://automationexercise.com")

# Verify home page
print(driver.title)

# Click on 'Products'
driver.find_element(By.XPATH, "//a[@href='/products']").click()
time.sleep(2)

# Verify 'All Products' page
print("All Products" in driver.page_source)

# Check products list
products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
print(len(products))

# Click 'View Product' of first product
driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]").click()
time.sleep(2)

# Verify product detail page
print(driver.current_url)

# Check product details
print(driver.find_element(By.XPATH, "//h2").text)
print(driver.find_element(By.XPATH, "//p[contains(text(),'Category')]").text)
print(driver.find_element(By.XPATH, "//span[contains(text(),'Rs.')]").text)
print(driver.find_element(By.XPATH, "//b[contains(text(),'Availability')]").text)
print(driver.find_element(By.XPATH, "//b[contains(text(),'Condition')]").text)
print(driver.find_element(By.XPATH, "//b[contains(text(),'Brand')]").text)

driver.quit()
