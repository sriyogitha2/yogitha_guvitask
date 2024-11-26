from selenium import webdriver  # Importing the Selenium WebDriver for browser automation
from selenium.webdriver.common.by import By  # Importing 'By' to locate elements on the web page
from selenium.webdriver.chrome.service import Service  # Importing Service for managing ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manage the ChromeDriver version
from selenium.webdriver.support.ui import WebDriverWait  # Importing WebDriverWait to wait for elements
from selenium.webdriver.support import expected_conditions as EC  # Importing expected conditions for element waits
from time import sleep  # Importing sleep for simple delays


class Data:
    # Class to store static data such as URLs
    url = "https://www.instagram.com/guviofficial/"


class GuviAutomation:
    
    def __init__(self):  # Constructor to initialize the browser driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Installs and starts ChromeDriver
    
    def start_automation(self):
        # Function to start browser automation
        self.driver.get(Data.url)  # Opens the specified URL
        self.driver.maximize_window()  # Maximizes the browser window
        sleep(5)  # Waits for the page to load completely
        
        self.close_login_popups()  # Calls the method to handle pop-ups
    
    def close_login_popups(self):
        # Function to handle and close the login pop-up if it appears
        try:
            login_popup_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))  # Waits until the close button is clickable
            )
            login_popup_close_button.click()  # Clicks the close button
            print("Login pop-up closed.")  # Logs the success message
            sleep(2)  # Waits after closing the pop-up
        except Exception:
            print("Login pop-up not found or already closed.")  # Logs if the pop-up wasn't found or closed already
    
    def fetch_following(self):
        # Function to fetch the count of users being followed
        try:
            following_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following')]//span"))  # Waits until the following element is present
            )
            return following_elem.text  # Returns the text content of the element (following count)
        except Exception as e:
            print(f"Error while fetching following count: {e}")  # Logs the error if fetching fails
            return None  # Returns None in case of failure
    
    def fetch_follower(self):
        # Function to fetch the count of followers
        try:
            follower_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]//span"))  # Waits until the followers element is present
            )
            return follower_elem.text  # Returns the text content of the element (followers count)
        except Exception as e:
            print(f"Error while fetching follower count: {e}")  # Logs the error if fetching fails
            return None  # Returns None in case of failure
    
    def shutdown(self):
        # Function to close the browser and clean up
        self.driver.quit()  # Quits the browser driver


# Instantiate and execute
guvi_insta = GuviAutomation()  # Creates an instance of the GuviAutomation class
guvi_insta.start_automation()  # Starts the automation process

# Fetch the counts for following and followers
following_count = guvi_insta.fetch_following()  # Calls the method to fetch the following count
follower_count = guvi_insta.fetch_follower()  # Calls the method to fetch the followers count

# Print the results
if following_count and follower_count:  # Checks if both counts are successfully fetched
    print("Following:", following_count)  # Prints the following count
    print("Followers:", follower_count)  # Prints the followers count
else:
    print("Couldn't fetch the counts.")  # Logs a failure message if counts are unavailable

guvi_insta.shutdown()  # Closes the browser and ends the script
