import pytest
import sys
import os
import time
from pages.login_page import LoginPage
from utils.driver_setup import DriverSetup
from selenium.webdriver.common.by import By

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def driver():
    driver = DriverSetup().initialize_driver()
    yield driver
    driver.quit()

# Test-Case-8: Checkout, Verify Products, Screenshot, and Finish Checkout
def test_checkout_process_verification(driver):
    print("\nStarting test: test_checkout_process_verification")
    login_page = LoginPage(driver)

    # Step 1: Login to the application
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)

    # Step 2: Add first 4 products to the cart
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(product_elements) >= 4, "Not enough products available for the test."

    selected_products = []
    for product in product_elements[:4]:
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        product.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
        selected_products.append((product_name, product_price))
        time.sleep(1)
    print("Selected 4 products added to the cart:", selected_products)

    # Step 3: Navigate to the Cart
    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)

    # Step 4: Start the Checkout Process
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)

    # Step 5: Enter Personal Details
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Step 6: Verify Product Details on the Checkout Overview Page
    checkout_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    checkout_products = []
    for item in checkout_items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        checkout_products.append((name, price))

    print("Products on Checkout Overview:", checkout_products)
    assert checkout_products == selected_products, "Product details do not match between cart and overview page."

    # Step 7: Take a Screenshot of Checkout Overview
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, "checkout_overview.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

    # Step 8: Finish Checkout Process
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Step 9: Verify Checkout Confirmation
    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message == "Thank you for your order!", "Checkout confirmation message does not match!"
    print("Checkout completed successfully with confirmation:", confirmation_message)

    print("Test test_checkout_process_verification passed successfully.")
