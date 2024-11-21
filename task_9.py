from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class SauceDemo:
    def __init__(self, url):
        self.url = url  # Initialize with the URL passed to the class
        self.driver = webdriver.Chrome()  # Set up ChromeDriver

    def start_automation(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)

    def fetch_title(self):
        SauceDemo_title = self.driver.title
        print(f"Page Title: {SauceDemo_title}")  # Print the page title
        return SauceDemo_title

    def fetch_url(self):
        SauceDemo_url = self.driver.current_url
        print(f"Current URL: {SauceDemo_url}")  # Print the current URL
        return SauceDemo_url

    # Saving the page content directly
    def save_page_content(self):
        page_content = self.driver.page_source
        file = open("Webpage_task_11.txt", "w")  # Open the file for writing
        file.write(page_content)  # Write the HTML content
        file.close()  # Close the file
        print("Page content saved to Webpage_task_11.txt")  # Print confirmation

    def close_browser(self):
        self.driver.quit()  # Close the browser


# URL to be tested
url = "https://www.saucedemo.com/"
automation = SauceDemo(url)  # Create an instance of SauceDemo

# Start the browser and navigate to the URL
automation.start_automation()

# Fetch and print the title and URL
automation.fetch_title()  # Fetch and print the page title
automation.fetch_url()  # Fetch and print the current URL

# Save the page content directly
automation.save_page_content()

# Close the browser
automation.close_browser()
