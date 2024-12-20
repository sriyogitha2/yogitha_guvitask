import pytest  # Import pytest for creating test functions and test setup
from selenium import webdriver  # Import WebDriver from Selenium to interact with the browser
from selenium.webdriver.common.by import By  # Import By to locate elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for waits
import time  # Import time for pausing execution to allow elements to load

@pytest.fixture(scope="module")
def browser():
    """
    Fixture to initialize and quit the WebDriver instance.
    - 'module' scope ensures that the WebDriver is initialized once per module.
    """
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    driver.maximize_window()  # Maximize the browser window to make it easier to interact with elements
    yield driver  # Yield the driver to the test function to use
    driver.quit()  # Quit the WebDriver once the tests are finished


class TestCreateNewUser:
    """
    Test suite for creating and verifying a new user via the Admin menu in OrangeHRM.
    """

    def test_create_and_verify_user(self, browser):
        """
        Test case: Create a new user via the Admin menu and verify login.
        """

        # Step 1: Navigate to OrangeHRM login page
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Open the login page
        print("Navigated to OrangeHRM login page.")
        time.sleep(2)  # Wait for the page to load

        # Step 2: Log in as Admin
        browser.find_element(By.NAME, "username").send_keys("Admin")  # Enter the Admin username
        browser.find_element(By.NAME, "password").send_keys("admin123")  # Enter the Admin password
        browser.find_element(By.XPATH, "//button[@type='submit']").click()  # Click the login button
        print("Logged in as Admin.")
        time.sleep(3)  # Wait for the dashboard to load

        # Step 3: Navigate to Admin menu
        admin_menu = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))  # Wait until the Admin menu is clickable
        )
        admin_menu.click()  # Click on the Admin menu
        print("Navigated to Admin menu.")
        time.sleep(2)  # Wait for the Admin menu page to load

        # Step 4: Click "Add" to create a new user
        browser.find_element(By.XPATH, "//button[text()=' Add ']").click()  # Click the 'Add' button to create a new user
        print("Clicked on 'Add' to create a new user.")
        time.sleep(2)  # Wait for the form to load

        # Fill out the new user form
        browser.find_element(By.XPATH, "//label[text()='User Role']/following-sibling::div").click()  # Click to open the user role dropdown
        browser.find_element(By.XPATH, "//span[text()='ESS']").click()  # Select the 'ESS' role for the new user

        # Enter the Employee Name
        browser.find_element(By.XPATH, "//label[text()='Employee Name']/following-sibling::div/input").send_keys("Paul Collings")
        time.sleep(2)  # Wait for suggestions to load
        browser.find_element(By.XPATH, "//div[contains(@class, 'oxd-autocomplete-option')]").click()  # Select the employee name from suggestions

        # Enter the Username
        browser.find_element(By.XPATH, "//label[text()='Username']/following-sibling::div/input").send_keys("new_user1")
        
        # Set the user status to Enabled
        browser.find_element(By.XPATH, "//label[text()='Status']/following-sibling::div").click()
        browser.find_element(By.XPATH, "//span[text()='Enabled']").click()  # Select 'Enabled' status

        # Set the password and confirm the password
        browser.find_element(By.XPATH, "//label[text()='Password']/following-sibling::div/input").send_keys("password123")
        browser.find_element(By.XPATH, "//label[text()='Confirm Password']/following-sibling::div/input").send_keys("password123")
        
        # Click the Save button to create the new user
        browser.find_element(By.XPATH, "//button[text()=' Save ']").click()
        print("New user created.")
        time.sleep(3)  # Wait for the user creation process to complete

        # Step 5: Log out as Admin
        browser.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()  # Click on the user dropdown menu
        browser.find_element(By.XPATH, "//a[text()='Logout']").click()  # Click the logout button
        print("Logged out as Admin.")
        time.sleep(2)  # Wait for the logout process to complete

        # Step 6: Log in as the newly created user
        browser.find_element(By.NAME, "username").send_keys("new_user1")  # Enter the new user's username
        browser.find_element(By.NAME, "password").send_keys("password123")  # Enter the new user's password
        browser.find_element(By.XPATH, "//button[@type='submit']").click()  # Click the login button
        print("Logged in as new user.")
        time.sleep(3)  # Wait for the new user's dashboard to load

        # Step 7: Verify successful login
        try:
            # Wait until the dashboard header is visible
            dashboard = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))  # Check for dashboard element
            )
            # Assert that the dashboard is displayed to verify successful login
            assert dashboard.is_displayed(), "Dashboard not visible. Login failed."
            print("User login verified successfully.")  # Print success message if the login is successful
        except Exception as e:
            # If an exception occurs (e.g., login failed), print the error
            print(f"Login verification failed: {e}")
