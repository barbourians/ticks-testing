from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#driver = webdriver.Chrome()
