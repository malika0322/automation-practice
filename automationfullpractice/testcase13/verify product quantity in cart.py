from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1 & 2. Launch browser and navigate to URL
driver.get("http://automationexercise.com")
time.sleep(2)

# 3. Verify home page is visible
print("Home Page Visible:", "Automation Exercise" in driver.title)

# 4. Click 'View Product' for first product on home page
driver.execute_script("window.scrollBy(0, 400);")  # scroll to make product visible
time.sleep(2)
driver.find_element(By.XPATH, "(//a[text()='View Product'])[1]").click()
time.sleep(2)

# 5. Verify product detail page opened
print("Product Detail Page:", "product_details" in driver.current_url)

# 6. Increase quantity to 4
qty_box = driver.find_element(By.ID, "quantity")
qty_box.clear()
qty_box.send_keys("4")
time.sleep(1)

# 7. Click 'Add to cart' button (fixed XPath)
driver.find_element(By.XPATH, "//button[contains(.,'Add to cart')]").click()
time.sleep(2)

# 8. Click 'View Cart' button
driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
time.sleep(2)

# 9. Verify product quantity in cart
cart_qty = driver.find_element(By.XPATH, "//td[@class='cart_quantity']").text
print("Quantity in Cart:", cart_qty)
print("Correct Quantity (4):", cart_qty.strip() == "4")

driver.quit()
