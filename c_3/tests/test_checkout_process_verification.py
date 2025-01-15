# Import necessary modules for testing
import pytest
import sys
import os
import time
from pages.login_page import LoginPage  # Import LoginPage class for login functionality
from utils.driver_setup import DriverSetup  # Import DriverSetup to initialize the driver
from selenium.webdriver.common.by import By  # For locating web elements

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

# Test to verify the entire checkout process: adding products, verifying details, taking a screenshot, and confirming checkout
def test_checkout_process_verification(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_checkout_process_verification")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)

    # Step 1: Login to the application
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for the login process to complete

    # Step 2: Add first 4 products to the cart
    product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item")  # Locate product elements on the page
    # Assert that there are at least 4 products available for the test
    assert len(product_elements) >= 4, "Not enough products available for the test."

    # Select and add the first 4 products to the cart
    selected_products = []
    for product in product_elements[:4]:
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text  # Get product name
        product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text  # Get product price
        product.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()  # Add product to cart
        selected_products.append((product_name, product_price))  # Store selected product details
        time.sleep(1)  # Allow time for cart update
    print("Selected 4 products added to the cart:", selected_products)

    # Step 3: Navigate to the Cart
    driver.find_element(By.ID, "shopping_cart_container").click()  # Click on the cart button
    time.sleep(2)  # Wait for the cart page to load

    # Step 4: Start the Checkout Process
    driver.find_element(By.ID, "checkout").click()  # Click the checkout button
    time.sleep(1)  # Wait for the checkout page to load

    # Step 5: Enter Personal Details
    driver.find_element(By.ID, "first-name").send_keys("John")  # Enter first name
    driver.find_element(By.ID, "last-name").send_keys("Doe")  # Enter last name
    driver.find_element(By.ID, "postal-code").send_keys("12345")  # Enter postal code
    driver.find_element(By.ID, "continue").click()  # Click continue
    time.sleep(2)  # Wait for the next page to load

    # Step 6: Verify Product Details on the Checkout Overview Page
    checkout_items = driver.find_elements(By.CLASS_NAME, "cart_item")  # Get items in the checkout overview
    checkout_products = []
    for item in checkout_items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text  # Get product name in overview
        price = item.find_element(By.CLASS_NAME, "inventory_item_price").text  # Get product price in overview
        checkout_products.append((name, price))  # Store product details

    print("Products on Checkout Overview:", checkout_products)
    # Assert that the products in the cart match the products in the checkout overview
    assert checkout_products == selected_products, "Product details do not match between cart and overview page."

    # Step 7: Take a Screenshot of Checkout Overview
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")  # Define directory for screenshots
    if not os.path.exists(screenshot_dir):  # Create the directory if it does not exist
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, "checkout_overview.png")  # Define screenshot file path
    driver.save_screenshot(screenshot_path)  # Save screenshot
    print(f"Screenshot saved at: {screenshot_path}")

    # Step 8: Finish Checkout Process
    driver.find_element(By.ID, "finish").click()  # Click the finish button to complete checkout
    time.sleep(2)  # Wait for the completion page to load

    # Step 9: Verify Checkout Confirmation
    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text  # Get confirmation message
    # Assert that the confirmation message matches the expected text
    assert confirmation_message == "Thank you for your order!", "Checkout confirmation message does not match!"
    print("Checkout completed successfully with confirmation:", confirmation_message)

    # Print a message indicating the test has passed successfully
    print("Test test_checkout_process_verification passed successfully.")
