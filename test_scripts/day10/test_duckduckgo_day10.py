from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from duckduckgo_home import DuckDuckGoHomePage
from duckduckgo_result import DuckDuckGoResultsPage

def test_duckduckgo_search():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    home = DuckDuckGoHomePage(driver)
    home.load()
    home.search("Selenium Python")

    results = DuckDuckGoResultsPage(driver)
    time.sleep(2)  # (will replace with waits later)

    assert "Selenium" in results.first_result_text()

    driver.quit()
