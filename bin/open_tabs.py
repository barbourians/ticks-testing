import time 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants
ROOM = "m2"
URL = "http://localhost:8080"  # Change this to your app's URL

# Path to ChromeDriver
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"  # Update this with your actual path

# Create a Service instance
service = Service(CHROMEDRIVER_PATH)

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

def main():
    
    # Tick setting to allow multiple users
    url = URL+"/settings"
    driver.execute_script(f"window.open('{url}', '_blank');")
    time.sleep(5)
    
    # Open tutor page
    url = URL+"/"+ROOM+"/tutor"
    driver.execute_script(f"window.open('{url}', '_blank');")
    time.sleep(2)
    
    # Open tabs
    for _ in range(20):
        url = URL+"/"+ROOM
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(5)

    # Open poll page
    url = URL+"/"+ROOM+"/poll"
    driver.execute_script(f"window.open('{url}', '_blank');")

    input("Press Enter to exit...")
    driver.quit()


if __name__ == "__main__":
    main()
