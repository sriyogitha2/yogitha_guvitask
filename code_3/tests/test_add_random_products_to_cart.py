# tests/test_add_random_products_to_cart.py
import pytest
import sys
import os
import random
from pages.login_page import LoginPage
from utils.driver_setup import DriverSetup
from selenium.webdriver.common.by import By
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def driver():
    driver = DriverSetup().initialize_driver()
    yield driver
    driver.quit()

# Test to randomly select 4 products, add them to cart, and verify the cart count
def test_add_random_products_to_cart(driver):
    print("\nStarting test: test_add_random_products_to_cart")
    login_page = LoginPage(driver)

    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login to complete
    
    # Step 2: Locate all product elements on the inventory page
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(product_elements) == 6, "Expected 6 products, but found a different number."

    # Step 3: Randomly select 4 products
    selected_products = random.sample(product_elements, 4)
    
    # Step 4: Add the selected products to the cart
    for idx, product in enumerate(selected_products, start=1):
        add_to_cart_button = product.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_to_cart_button.click()
        print(f"Added Product {idx}: {product_name} to cart.")
        time.sleep(1)  # Allow time for cart to update

    # Step 5: Verify that the cart shows 4 items
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "4", f"Cart count mismatch! Expected 4, but got {cart_count}."
    print("Cart button displays the correct count of 4 products.")

    print("Test test_add_random_products_to_cart passed successfully.")
