from time import sleep  # Import sleep to pause the execution for a specified duration
from selenium import webdriver  # Import the WebDriver class from Selenium
from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for waits


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
        element = self.driver.find_element(by, value)  # Find the element by its locator (e.g., ID, XPath, etc.)
        element.click()  # Perform a click action on the located element
        sleep(3)  # Sleep for 3 seconds to ensure the next page or interaction is ready

    def wait_for_element(self, by, value, timeout=10):
        """Wait for an element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))  # Wait until the element is clickable within the timeout period
        )

    def quit_driver(self):
        """Quit the WebDriver and close the browser."""
        self.driver.quit()  # Close all browser windows and terminate the WebDriver session
