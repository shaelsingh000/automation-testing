import pytest
import logging
from test_scripts.day13.pages.duckduckgo_home import DuckDuckGoHomePage
from test_scripts.day13.pages.duckduckgo_result import DuckDuckGoResultsPage

search_terms = ["Selenium Python", "Pytest Tutorial", "Automation Testing"]

@pytest.mark.parametrize("term", search_terms)
def test_duckduckgo_search(driver, term):
    logging.info(f"Starting search test for: {term}")

    home = DuckDuckGoHomePage(driver)
    home.load()
    home.search(term)

    results = DuckDuckGoResultsPage(driver)
    first_result = results.get_first_result_text()

    logging.info(f"First result for {term}: {first_result}")
    assert term.split()[0].lower() in first_result.lower()
