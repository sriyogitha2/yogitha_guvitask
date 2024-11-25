from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

#import the action chains class for performing complex user interactions
from selenium.webdriver.common.action_chains import ActionChains

# Data class to store the URL
class Data:
    url="https://jqueryui.com/droppable/"

# Locators class to store the element locators and iframe locator
class Locators:
    source_element_locator='draggable'   # Locator for the source element to be dragged
    target_element_locator='droppable'   # Locator for the target element to drop the source element
    iframe_locator = 'iframe'            # Locator for the iframe that contains the draggable and droppable elements

# DragandDrop class that inherits from Data and Locators
class DragandDrop(Data, Locators):
    def __init__(self):
        # Initialize the Firefox WebDriver and ActionChains object
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action = ActionChains(self.driver)

    def drag_drop(self):
        try:
            # Maximize the browser window
            self.driver.maximize_window()
            # Navigate to the URL
            self.driver.get(self.url)
            # Sleep for 10 seconds to let the page load completely
            sleep(10)

            # Find the iframe element on the page
            iframe = self.driver.find_element(by=By.CSS_SELECTOR, value='iframe')
            # Switch the context to the iframe to interact with elements inside it
            self.driver.switch_to.frame(iframe)

            # Locate the source (draggable) and target (droppable) elements inside the iframe
            source_element = self.driver.find_element(by=By.ID, value=self.source_element_locator)
            target_element = self.driver.find_element(by=By.ID, value=self.target_element_locator)
     
            # Use ActionChains to perform the drag and drop action
            self.action.drag_and_drop(source_element, target_element).perform()

            # Print success message after drag-and-drop is completed
            print("Success: drag and drop")
        except(NoSuchElementException, ElementNotVisibleException) as error:
            # Handle exceptions when elements are not found or not visible
            print("Element is not visible", error)
        finally:
            # Quit the driver and close the browser window
            self.driver.quit()

# Create an instance of the DragandDrop class and call the drag_drop method
myActions = DragandDrop()
myActions.drag_drop()
