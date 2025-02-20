import pytest
import requests

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

def test_tutor_page_contains_name(driver):
    page = f"{BASE_URL}/TEST/tutor"
    
    # Check the HTTP status code using requests
    response = requests.get(page)
    assert response.status_code == 200

    # Load the page and wait for Angular to render
    driver.get(page)  
    driver.implicitly_wait(2)  
    
    # Find the text on the page
    assert "Room TEST" in driver.page_source, "Text 'Room TEST' not found on the learner page"


def test_learner_page_contains_name(driver):
    page = f"{BASE_URL}/TEST"
    
    # Check the HTTP status code using requests
    response = requests.get(page)
    assert response.status_code == 200

    # Load the page and wait for Angular to render
    driver.get(page)  
    driver.implicitly_wait(2)  # Wait for Angular to render
    
    # Find the text on the page
    assert "Room TEST" in driver.page_source, "Text 'Room TEST' not found on the learner page"

