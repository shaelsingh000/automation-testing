import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from duckduckgo_homepage import DuckDuckGoHomePage

@pytest.mark.parametrize("search_term", ["Selenium Python", "Automation Testing", "Pytest Tutorial"])
def test_duckduckgo_search(search_term):
    driver = webdriver.Chrome()
    page = DuckDuckGoHomePage(driver)

    # Load page and perform search
    page.load()
    page.search(search_term)

    time.sleep(2)

    assert search_term.lower() in driver.page_source.lower()

    driver.quit()
