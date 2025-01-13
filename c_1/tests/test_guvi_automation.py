from asyncio import sleep
import pytest
from utils.webdriver_helper import WebDriverHelper  # Import helper class for WebDriver operations.
from pages.home_page import HomePage               # Import page object model for the home page.
from pages.login_page import LoginPage             # Import page object model for the login page.
from selenium.webdriver.common.by import By        # Import By for locating elements.
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits.
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for waits.
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Import exceptions for handling errors.


@pytest.fixture(scope="class")  # Define a fixture with class-level scope for reusability across tests.
def setup():
    """Fixture for setting up WebDriver and page objects."""
    print("Initializing WebDriver and page objects")  # Log initialization.
    driver_helper = WebDriverHelper()  # Create an instance of WebDriverHelper.
    driver = driver_helper.driver  # Access the WebDriver instance.
    driver_helper.driver.maximize_window()  # Maximize the browser window.
    driver_helper.driver.implicitly_wait(10)  # Set an implicit wait of 10 seconds.

    home_page = HomePage(driver)  # Instantiate the HomePage object.
    login_page = LoginPage(driver)  # Instantiate the LoginPage object.

    yield driver_helper, home_page, login_page  # Yield the driver helper and page objects for tests.

    print("Closing WebDriver session")  # Log teardown.
    driver_helper.quit_driver()  # Quit the WebDriver instance.


class TestGuviAutomation:
    """Test class for automating login and signup on the Guvi website."""

    def test_valid_url(self, setup):
        """Test if the homepage URL is valid."""
        print("Starting test: test_valid_url")  # Log test initiation.
        driver_helper, home_page, _ = setup  # Retrieve setup objects.
        driver_helper.navigate("https://www.guvi.in/")  # Navigate to the Guvi homepage.
        assert driver_helper.driver.current_url == "https://www.guvi.in/"  # Validate the current URL.
        print("URL is valid: PASS")  # Log test result.

    def test_homepage_title(self, setup):
        """Test if the homepage title is correct."""
        print("Starting test: test_homepage_title")  # Log test initiation.
        driver_helper, home_page, _ = setup  # Retrieve setup objects.
        driver_helper.navigate("https://www.guvi.in/")  # Navigate to the Guvi homepage.
        assert driver_helper.driver.title == "GUVI | Learn to code in your native language"  # Validate the title.
        print("Homepage title is valid: PASS")  # Log test result.

    def test_login_button_visibility(self, setup):
        """Test if the login button is visible on the homepage."""
        print("Starting test: test_login_button_visibility")  # Log test initiation.
        _, home_page, _ = setup  # Retrieve setup objects.
        assert home_page.LOGIN_BTN is not None, "Login button is not visible"  # Assert login button visibility.
        print("Login button is visible: PASS")  # Log test result.

    def test_signup_visibility(self, setup):
        """Test if the sign-up button is visible on the homepage."""
        print("Starting test: test_signup_visibility")  # Log test initiation.
        _, home_page, _ = setup  # Retrieve setup objects.
        assert home_page.SIGNUP_BTN is not None, "Sign-up button is not visible"  # Assert sign-up button visibility.
        print("Sign-up button is visible: PASS")  # Log test result.

    def test_valid_and_invalid_login(self, setup):
        """Test valid login followed by invalid login with a fresh session."""
        print("Starting test: test_valid_and_invalid_login")  # Log test initiation.
        driver_helper, home_page, login_page = setup  # Retrieve setup objects.

        # Step 1: Perform valid login
        print("Performing valid login")  # Log valid login step.
        driver_helper.navigate("https://www.guvi.in")  # Navigate to the Guvi homepage.
        home_page.click_login()  # Click the login button on the homepage.
        login_page.login("sriyogithaselvaraj2001@gmail.com", "22-Nov-2001")  # Perform login with valid credentials.
        WebDriverWait(driver_helper.driver, 10).until(  # Wait until the page title contains 'courses'.
            lambda d: "courses" in d.title.lower()
        )
        assert "courses" in driver_helper.driver.title.lower(), "Valid login failed"  # Assert valid login success.
        print("Valid login test completed: PASS")  # Log valid login result.

        # Step 2: Close the browser session after valid login
        print("Closing browser session after valid login")  # Log session closure.
        driver_helper.quit_driver()  # Quit the WebDriver session.

        # Step 3: Start a new session for invalid login
        print("Starting a new browser session for invalid login")  # Log new session initiation.
        new_driver_helper = WebDriverHelper()  # Create a new WebDriverHelper instance.
        new_driver_helper.navigate("https://www.guvi.in")  # Navigate to the Guvi homepage.
        new_home_page = HomePage(new_driver_helper.driver)  # Instantiate the HomePage object for the new session.
        new_login_page = LoginPage(new_driver_helper.driver)  # Instantiate the LoginPage object for the new session.

        # Step 4: Attempt invalid login
        print("Attempting invalid login")  # Log invalid login step.
        new_home_page.click_login()  # Click the login button on the homepage.
        new_login_page.login("invalidemail@example.com", "wrongpassword")  # Perform login with invalid credentials.

        # Step 5: Validate error message
        print("Validating error message for invalid login")  # Log error message validation step.
        expected_msg = "Incorrect Email or Password"  # Expected error message text.
        try:
            err_msg = WebDriverWait(new_driver_helper.driver, 10).until(  # Wait for error message to appear.
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Incorrect Email or Password')]"))
            )
            assert err_msg.text.strip() == expected_msg, f"Unexpected error message: '{err_msg.text.strip()}'"  # Validate error message.
            print("Error message validation completed: PASS")  # Log validation success.
        except TimeoutException:
            print("Error: Error message not displayed for invalid login")  # Log validation failure.
            assert False, "Error message not displayed after invalid login"  # Fail the test if no error message.

        # Step 6: Quit the new session
        print("Closing browser session after invalid login test")  # Log session closure.
        new_driver_helper.quit_driver()  # Quit the WebDriver session.
