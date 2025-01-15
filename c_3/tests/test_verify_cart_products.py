# Import necessary modules for testing
import pytest
import sys
import os
from pages.login_page import LoginPage  # Import the LoginPage class for performing login actions
from utils.driver_setup import DriverSetup  # Import DriverSetup for initializing the WebDriver
from selenium.webdriver.common.by import By  # Import the By class to locate elements
import time  # Import time for managing delays in tests

# Modify system path to include the parent directory for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Pytest fixture to set up the WebDriver instance for the entire module
@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver instance
    driver = DriverSetup().initialize_driver()
    # Yield the driver to the tests, and quit the driver after the tests are completed
    yield driver
    driver.quit()

# Test to verify the products added to the cart
def test_verify_cart_products(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_verify_cart_products")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)

    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login to complete

    # Step 2: Navigate to inventory page and add 4 random products to the cart
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # Ensure there are 6 products available on the page
    assert len(product_elements) == 6, "Expected 6 products, but found a different number."

    selected_products = []  # List to store the details of selected products
    for product in product_elements[:4]:  # Select first 4 products for simplicity
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text  # Get product name
        product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text  # Get product price
        add_to_cart_button = product.find_element(By.CSS_SELECTOR, "button.btn_inventory")  # Locate the add to cart button
        add_to_cart_button.click()  # Add the product to the cart
        selected_products.append((product_name, product_price))  # Append product details to selected products list
        time.sleep(1)  # Allow time for cart update
    
    # Print the products that were added to the cart
    print("Added the following products to the cart:")
    for idx, (name, price) in enumerate(selected_products, start=1):
        print(f"Product {idx}: {name} - {price}")

    # Step 3: Click the Cart button to view the cart
    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
    time.sleep(2)  # Wait for the cart page to load

    # Step 4: Fetch product details from the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    cart_products = []  # List to store product details from the cart
    for item in cart_items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text  # Get product name from cart
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text  # Get product price from cart
        cart_products.append((name, price))  # Append product details from cart to the list

    # Step 5: Verify that the cart contains the same products as added
    print("Products in the cart:")
    for idx, (name, price) in enumerate(cart_products, start=1):
        print(f"Cart Product {idx}: {name} - {price}")

    # Assert that the products in the cart match the selected products
    assert cart_products == selected_products, "Cart products do not match the added products!"
    print("Cart contains the correct products.")

    # Print a message indicating the test passed successfully
    print("Test test_verify_cart_products passed successfully.")