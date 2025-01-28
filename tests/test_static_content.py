import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI

PAGE_WAIT = 2  # Seconds wait for Angular to render
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


def test_about_page_contains(driver):
    driver.get(f"{BASE_URL}/about")  # Load the page

    driver.implicitly_wait(PAGE_WAIT)  # Wait for Angular to render  
     
    # Find the text on the page
    assert "About QA Ticks and Crosses" in driver.page_source, "Text 'About QA Ticks and Crosses' not found on the About page"



