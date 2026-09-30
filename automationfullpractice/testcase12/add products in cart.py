from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("http://automationexercise.com")
time.sleep(2)

# Verify home page
print("Home Page Visible:", "Automation Exercise" in driver.title)

# Click Products
driver.find_element(By.XPATH, "//a[@href='/products']").click()
time.sleep(2)

# -------------------- FIRST PRODUCT --------------------
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

first_card = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center'])[1]")
actions.move_to_element(first_card).perform()
time.sleep(1)

first_add = driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]")
driver.execute_script("arguments[0].click();", first_add)
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()
time.sleep(2)

# -------------------- SECOND PRODUCT --------------------

# Extra scroll to avoid ad blocking
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

second_card = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center'])[2]")
actions.move_to_element(second_card).perform()
time.sleep(1)

second_add = driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[2]")
driver.execute_script("arguments[0].click();", second_add)
time.sleep(2)

# Click View Cart
driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
time.sleep(2)

# -------------------- VERIFY CART ITEMS --------------------
cart_items = driver.find_elements(By.XPATH, "//tr[contains(@id,'product')]")
print("Products in cart:", len(cart_items))
print("Both products added:", len(cart_items) == 2)

# Verify price, qty, total for each product
for i in range(1, len(cart_items) + 1):
    price = driver.find_element(By.XPATH, f"(//td[@class='cart_price']/p)[{i}]").text
    qty = driver.find_element(By.XPATH, f"(//td[@class='cart_quantity'])[{i}]").text
    total = driver.find_element(By.XPATH, f"(//td[@class='cart_total']/p)[{i}]").text
    print(f"Product {i} -> Price: {price} | Qty: {qty} | Total: {total}")

driver.quit()
