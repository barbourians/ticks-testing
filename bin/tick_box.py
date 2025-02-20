import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"  # Update this with your actual path

# Initialize WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("http://localhost:8080")  # Replace with your URL

# Wait until the checkbox is present and clickable
try:
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "use-session"))
    )
    # Click the checkbox
    checkbox.click()
    print("Checkbox clicked!")
except Exception as e:
    print(f"Error: {e}")


# Wait and then close everything
input("Press Enter to exit...")
driver.quit()
