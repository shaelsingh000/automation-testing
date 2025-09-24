import pytest
from pages.duckduckgo_page import DuckDuckGoPage
from utils.logger import get_logger

logger = get_logger("DuckDuckGoTest")

# Data-driven search terms
search_terms = ["Selenium Python", "Pytest Tutorial", "Automation Testing"]

@pytest.mark.parametrize("search_term", search_terms)
def test_duckduckgo_search(driver, search_term):
    logger.info(f"Starting test with search term: {search_term}")

    page = DuckDuckGoPage(driver)
    page.open_homepage()
    logger.info("Opened DuckDuckGo homepage")

    page.search(search_term)
    logger.info(f"Searched for: {search_term}")

    assert page.is_search_successful(search_term)
    logger.info(f"✅ Search successful for: {search_term}")
