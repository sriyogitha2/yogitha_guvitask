# Import necessary modules for testing
import pytest
import sys
import os
import random
from pages.login_page import LoginPage  # Import LoginPage class for login functionality
from utils.driver_setup import DriverSetup  # Import DriverSetup to initialize the driver
from selenium.webdriver.common.by import By  # For locating web elements
import time  # For adding delays between actions

# Modify system path to include the parent directory for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Pytest fixture to set up the WebDriver instance for the entire module
@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver
    driver = DriverSetup().initialize_driver()
    # Yield the driver for use in the tests, and quit the driver after test completion
    yield driver
    driver.quit()

# Test to randomly select 4 products, add them to the cart, and verify the cart count
def test_add_random_products_to_cart(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_add_random_products_to_cart")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)

    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for the login process to complete
    
    # Step 2: Locate all product elements on the inventory page
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # Verify that 6 products are displayed, else raise an assertion error
    assert len(product_elements) == 6, "Expected 6 products, but found a different number."

    # Step 3: Randomly select 4 products from the list of product elements
    selected_products = random.sample(product_elements, 4)
    
    # Step 4: Add the selected products to the cart
    for idx, product in enumerate(selected_products, start=1):
        # Locate the 'Add to Cart' button for the product
        add_to_cart_button = product.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        # Get the product name to print in the log
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        # Click the 'Add to Cart' button
        add_to_cart_button.click()
        # Print which product was added to the cart
        print(f"Added Product {idx}: {product_name} to cart.")
        time.sleep(1)  # Allow time for the cart to update after each action

    # Step 5: Verify that the cart shows the correct number of items
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    # Assert that the cart count is 4, otherwise print an error message
    assert cart_count == "4", f"Cart count mismatch! Expected 4, but got {cart_count}."
    # Print confirmation message for successful cart count verification
    print("Cart button displays the correct count of 4 products.")

    # Print a message indicating that the test has passed successfully
    print("Test test_add_random_products_to_cart passed successfully.")

