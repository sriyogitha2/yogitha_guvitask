from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Data:
    url = "https://www.instagram.com/guviofficial/"

class GuviAutomation:
    
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    def start_automation(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(20)  
    
    def fetch_following(self):
        
        sleep(5)  
        following_elem = self.driver.find_element(By.XPATH, "//span[contains(text(), ' following')]")
        return following_elem.text
    
    def fetch_follower(self):
        
        sleep(5)  
        follower_elem = self.driver.find_element(By.XPATH, "//span[contains(text(), ' followers')]")
        return follower_elem.text
    
    def shutdown(self):
        self.driver.quit()

guvi_insta = GuviAutomation()
guvi_insta.start_automation()

# Fetch the counts for following and followers
following_count = guvi_insta.fetch_following()
follower_count = guvi_insta.fetch_follower()

# Print the results
if following_count and follower_count:
    print("Following:", following_count)
    print("Followers:", follower_count)
else:
    print("Couldn't fetch the counts.")

guvi_insta.shutdown()