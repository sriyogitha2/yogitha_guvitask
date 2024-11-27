from selenium import webdriver  # Importing the Selenium webdriver module
from selenium.webdriver.common.by import By  # Importing the By class for locating elements
from selenium.webdriver.firefox.service import Service  # Importing the Service class for Firefox driver
from webdriver_manager.firefox import GeckoDriverManager  # Importing GeckoDriverManager for automatic Firefox driver setup
from time import sleep  # Importing sleep for adding delays

# Defining a class to hold the URL for the automation script
class Data:
    url = "https://www.instagram.com/guviofficial/"  # URL of the Instagram page to scrape

# Defining the main automation class
class GuviAutomation:
    
    # Constructor to initialize the Firefox WebDriver
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # Automatically installs and initializes Firefox WebDriver
    
    # Method to start automation by navigating to the URL and maximizing the browser window
    def start_automation(self):
        self.driver.get(Data.url)  # Open the URL in the browser
        self.driver.maximize_window()  # Maximize the browser window
        sleep(20)  # Wait for the page to load completely (adjustable delay)
    
    # Method to fetch the "following" count from the Instagram page
    def fetch_following(self):
        sleep(5)  # Add delay to ensure the page is fully loaded
        following_elem = self.driver.find_element(By.XPATH, "//span[contains(text(), ' following')]")  # Locate the "following" element
        return following_elem.text  # Return the text content of the element
    
    # Method to fetch the "follower" count from the Instagram page
    def fetch_follower(self):
        sleep(5)  # Add delay to ensure the page is fully loaded
        follower_elem = self.driver.find_element(By.XPATH, "//span[contains(text(), ' followers')]")  # Locate the "followers" element
        return follower_elem.text  # Return the text content of the element
    
    # Method to safely shut down the WebDriver
    def shutdown(self):
        self.driver.quit()  # Close the browser and end the WebDriver session

# Instantiate the GuviAutomation class
guvi_insta = GuviAutomation()
guvi_insta.start_automation()  # Start the automation process

# Fetch the counts for "following" and "followers"
following_count = guvi_insta.fetch_following()  # Call the method to get the "following" count
follower_count = guvi_insta.fetch_follower()  # Call the method to get the "followers" count

# Print the results
if following_count and follower_count:  # Check if both counts are successfully fetched
    print("Following:", following_count)  # Print the "following" count
    print("Followers:", follower_count)  # Print the "followers" count
else:
    print("Couldn't fetch the counts.")  # Print an error message if the counts are not fetched

guvi_insta.shutdown()  # Shut down the WebDriver
