from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1 & 2. Launch browser and open URL
driver.get("http://automationexercise.com")
time.sleep(2)

# 3. Verify home page is visible successfully
print("Home Page Visible:", "Automation Exercise" in driver.title)

# 4. Click on 'Products' button
driver.find_element(By.XPATH, "//a[@href='/products']").click()
time.sleep(2)

# 5. Verify user is navigated to ALL PRODUCTS page successfully
print("All Products Page Visible:", "All Products" in driver.page_source)

# 6. Enter product name in search input and click search button
driver.find_element(By.ID, "search_product").send_keys("shirt")
driver.find_element(By.ID, "submit_search").click()
time.sleep(2)

# 7. Verify 'SEARCHED PRODUCTS' is visible
searched_products_title = driver.find_element(By.XPATH, "//h2[text()='Searched Products']")
print("SEARCHED PRODUCTS Visible:", searched_products_title.is_displayed())

# 8. Verify all products related to search are visible
results = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']")
print("Number of searched products:", len(results))
print("Search results visible:", len(results) > 0)

driver.quit()
