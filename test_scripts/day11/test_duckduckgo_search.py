from test_scripts.day11.pages.duckduckgo_home import DuckDuckGoHomePage
from test_scripts.day11.pages.duckduckgo_result import DuckDuckGoResultsPage
import time

def test_duckduckgo_search(driver):  # fixture driver will be automatically injected
    home = DuckDuckGoHomePage(driver)
    home.load()
    home.search("Selenium Python")

    results = DuckDuckGoResultsPage(driver)
    time.sleep(2)  # replace later with WebDriverWait

    assert "Selenium" in results.first_result_text()
