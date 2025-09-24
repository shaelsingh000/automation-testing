import pytest
import allure
from pages.duckduckgo_page import DuckDuckGoPage
from utils.logger import get_logger

logger = get_logger("pytest")

search_terms = ["Selenium Python", "Pytest Tutorial", "Automation Testing"]

@pytest.mark.parametrize("search_term", search_terms)
def test_duckduckgo_search(driver, search_term):
    logger.info(f"Starting test with search term: {search_term}")
    page = DuckDuckGoPage(driver)

    page.open_homepage()
    logger.info("Opened DuckDuckGo homepage")

    page.search(search_term)
    logger.info(f"Searched for: {search_term}")

    results = page.get_results()
    assert any(search_term.lower() in r.lower() for r in results), \
        f"Search term '{search_term}' not found in results: {results}"
    logger.info(f"✅ Search successful for: {search_term}")
