import requests
from time import sleep  
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Helper class to interact with the WebDriver
class WebDriverHelper:
    """Helper class for interacting with the WebDriver."""
    
    def __init__(self):
        """Initialize the WebDriver instance."""
        self.driver = webdriver.Chrome()  # Initialize the WebDriver with ChromeDriver

    def navigate(self, url):
        """Navigate to a specified URL."""
        self.driver.get(url)  # Navigate to the specified URL
        sleep(3)  # Sleep for 3 seconds to wait for the page to load

    def click_element(self, by, value):
        """Click an element identified by its locator."""
        element = self.driver.find_element(by, value)  # Find the element by locator
        element.click()  # Click on the found element
        sleep(3)  # Sleep for 3 seconds to wait for the next page to load

    def wait_for_element(self, by, value, timeout=10):
        """Wait for an element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))  # Wait until the element is clickable
        )

    def quit_driver(self):
        """Quit the WebDriver and close the browser."""
        self.driver.quit()  # Close the browser and quit the WebDriver

# Function to check if a URL is valid (returns status code 200)
def check_url_exists(url):
    """Check if the provided URL exists and returns status code 200."""
    try:
        response = requests.get(url)  # Send a GET request to the URL
        return response.status_code == 200  # Return True if status code is 200
    except requests.exceptions.RequestException:
        return False  # Return False if any error occurs during the request

# Function to load a URL and click the Sign-Up button
def load_url_and_click_signup(url):
    """Load the URL and click the Sign-Up button."""
    driver_helper = WebDriverHelper()  # Create an instance of the WebDriverHelper
    driver_helper.navigate(url)  # Navigate to the provided URL
    sleep(3)  # Sleep for 3 seconds to wait for the page to load
    
    try:
        # Find and click the Sign-Up button by its XPath
        signup_button = driver_helper.driver.find_element(By.XPATH, "//a[text()='Sign Up']")
        signup_button.click()  # Click the Sign-Up button
        sleep(3)  # Sleep for 3 seconds to wait for the next page to load
        assert "Sign Up" in driver_helper.driver.title  # Ensure the sign-up page loads correctly
        print("Successfully clicked the 'Sign-Up' button and navigated to the sign-up page.")
    except Exception as e:
        print(f"Error clicking the 'Sign-Up' button: {e}")
    finally:
        driver_helper.quit_driver()  # Quit the driver after the operation

# Parametrized test to check URL existence and click Sign-Up button
@pytest.mark.parametrize("url", ["https://www.guvi.in/sign-in/"])
def test_url_and_signup_click(url):
    """Test if the URL exists and clicks the Sign-Up button."""
    assert check_url_exists(url) is True, f"URL {url} does not exist"  # Check if URL exists
    load_url_and_click_signup(url)  # Call function to load the URL and click the Sign-Up button
    print(f"Successfully checked and clicked the 'Sign-Up' button on {url}")

# Main test class for automating login and signup on the Guvi website
class TestGuviAutomation:
    """Test class for automating login and signup on the Guvi website."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up WebDriver before each test and quit after."""
        self.driver_helper = WebDriverHelper()  # Initialize the WebDriverHelper
        self.driver_helper.driver.maximize_window()  # Maximize the browser window
        self.driver_helper.driver.implicitly_wait(10)  # Set implicit wait for elements
        yield
        self.driver_helper.quit_driver()  # Quit the driver after the test is complete

    # Test to validate the homepage URL
    def test_valid_url(self):
        """Test if the homepage URL is valid."""
        url = "https://www.guvi.in/"
        self.driver_helper.navigate(url)  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        assert self.driver_helper.driver.current_url == url  # Ensure the current URL matches the expected one
        print("URL is valid: PASS")

    # Test to validate the homepage title
    def test_homepage_title(self):
        """Test if the homepage title is correct."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        assert self.driver_helper.driver.title == "GUVI | Learn to code in your native language"  # Check if the title is correct
        print("Homepage title is valid: PASS")

    # Test to check the visibility of the login button
    def test_login_button_visibility(self):
        """Test if the login button is visible on the homepage."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        login_button = self.driver_helper.driver.find_element(By.XPATH, "//a[@id='login-btn']")  # Find the login button
        assert login_button.is_displayed(), "Login button is not visible"  # Ensure the login button is visible
        print("Login button is visible: PASS")

    # Test to check if the login button is clickable
    def test_login_button_clickable(self):
        """Test if the login button is clickable on the homepage."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        login_button = self.driver_helper.wait_for_element(By.XPATH, "//a[@id='login-btn']")  # Wait for the login button to be clickable
        assert login_button.is_enabled(), "Login button is not clickable"  # Ensure the login button is clickable
        print("Login button is clickable: PASS")

    # Test to check the visibility of the sign-up button
    def test_signup_visibility(self):
        """Test if the sign-up button is visible on the homepage."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        signup_button = self.driver_helper.driver.find_element(By.XPATH, "//a[@class='bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']")  # Find the sign-up button
        assert signup_button.is_displayed(), "Sign-up button is not visible"  # Ensure the sign-up button is visible
        print("Sign-up button is visible: PASS")
    
    # Test to check if the sign-up button is clickable
    def test_signup_clickable(self):
        """Test if the sign-up button is clickable on the homepage."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        signup_button = self.driver_helper.wait_for_element(By.XPATH, "//a[@class='bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']")  # Wait for the sign-up button to be clickable
        assert signup_button.is_enabled(), "Sign-up button is not clickable"  # Ensure the sign-up button is clickable
        print("Sign-up button is clickable: PASS")
    
    # Test to check login with valid credentials
    def test_login(self):
        """Test for successful login with valid credentials."""
        self.driver_helper.navigate("https://www.guvi.in/")  # Navigate to the homepage
        self.driver_helper.click_element(By.ID, "login-btn")  # Click the login button
        
        # Enter valid credentials
        self.driver_helper.driver.find_element(By.ID, "email").send_keys("sriyogithaselvaraj2001@gmail.com")
        self.driver_helper.driver.find_element(By.ID, "password").send_keys("22-Nov-2001")
        self.driver_helper.click_element(By.ID, "login-btn")  # Submit the login form
        
        # Sleep to wait for the page to load after login
        sleep(3)
        
        # Check if login was successful by verifying if the user is on the correct page
        # For instance, checking if the "courses" page is loaded, or if a user profile element is visible
        assert "courses" in self.driver_helper.driver.title, f"Expected 'GUVI | courses', but got {self.driver_helper.driver.title}"

        print("Login with valid credentials is successful: PASS")


    # Test to check login with invalid credentials
    def test_invalid_login(self):
        """Test for invalid login credentials."""
        self.driver_helper.navigate("https://www.guvi.in")  # Navigate to the homepage
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load
        self.driver_helper.click_element(By.ID, "login-btn")  # Click the login button
        self.driver_helper.driver.find_element(By.ID, "email").send_keys("invalidemail@example.com")  # Enter invalid email
        self.driver_helper.driver.find_element(By.ID, "password").send_keys("wrongpassword")  # Enter invalid password
        self.driver_helper.click_element(By.ID, "login-btn")  # Click the login button to submit
        sleep(3)  # Sleep for 3 seconds to allow the page to fully load after login

        # Check for error message after failed login
        expected_msg = "Incorrect Email or Password"
        try:
            err_msg = WebDriverWait(self.driver_helper.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Incorrect Email or Password')]"))
            )
            display_error = err_msg.text.strip()
        except Exception as e:
            print(f"Error message element not found: {e}")
            display_error = ""

        assert display_error == expected_msg, f"Unexpected error message: '{display_error}'"
        print("Login with invalid credentials test completed: PASS")
