# Import necessary modules from selenium and webdriver_manager
from selenium import webdriver  # Import the WebDriver for Chrome browser
from selenium.webdriver.chrome.service import Service  # Import Service to manage ChromeDriver
from selenium.webdriver.chrome.options import Options  # Import Options to configure browser settings
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager to automatically download the correct chromedriver

class DriverSetup:
    # Method to initialize and configure the WebDriver for the Chrome browser
    def initialize_driver(self):
        # Create a Service object to automatically manage ChromeDriver (no need to manually download the driver)
        service = Service(ChromeDriverManager().install())  # Automatically fetch and install ChromeDriver
        
        # Create an Options object to configure browser options
        options = Options()
        options.add_argument("--start-maximized")  # Set the browser to open in maximized mode

        # Initialize the WebDriver with the configured Service and Options objects
        driver = webdriver.Chrome(service=service, options=options)
        
        # Return the configured WebDriver instance
        return driver

