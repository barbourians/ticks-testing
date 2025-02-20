import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI

BASE_URL = "http://localhost:8080"


@pytest.fixture(scope="function")
def driver():
    # Set up the driver (setup)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    yield driver  # This will pass the driver to the test function
    
    # Teardown (after the test is done)
    driver.quit()

def test_home_page_contains(driver):
    driver.get(f"{BASE_URL}/")  # Load the page
    driver.implicitly_wait(2)  # Wait for Angular to render
    
    # Find the text on the page
    assert "make up a unique room code" in driver.page_source, "Text 'make up a unique room code' not found on the home page"

def test_about_page_contains(driver):
    driver.get(f"{BASE_URL}/about")  # Load the page
    driver.implicitly_wait(2)  # Wait for Angular to render
    
    # Find the text on the page
    assert "About QA Ticks and Crosses" in driver.page_source, "Text 'About QA Ticks and Crosses' not found on the /about page"

def test_settings_page_contains(driver):
    driver.get(f"{BASE_URL}/settings")  # Load the page
    driver.implicitly_wait(2)  # Wait for Angular to render
    
    # Find the text on the page
    assert "Allow me to have different names" in driver.page_source, "Text 'Allow me to have different names' not found on the /settings page"

def test_browser_check_page_contains(driver):
    driver.get(f"{BASE_URL}/browser-check")  # Load the page
    driver.implicitly_wait(2)  # Wait for Angular to render
    
    # Find the text on the page
    assert "Browser Check" in driver.page_source, "Text 'Browser Check' not found on the /browser-check page"



