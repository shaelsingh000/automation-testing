import pytest
from pages.duckduckgo_page import DuckDuckGoPage
from utils.logger import logger


search_terms = ["Selenium Python", "Pytest Tutorial", "Automation Testing"]

@pytest.mark.parametrize("search_term", search_terms)
def test_duckduckgo_search(driver, search_term):
    logger.info(f"🚀 Starting test with search term: {search_term}")

    duckduckgo = DuckDuckGoPage(driver)
    duckduckgo.load()
    logger.info("🌐 Opened DuckDuckGo homepage")

    duckduckgo.search(search_term)
    logger.info(f"🔍 Searching for: {search_term}")

    # Get first search result
    first_result = duckduckgo.get_first_result().text
    logger.info(f"First result text: {first_result}")

    assert search_term.split()[0].lower() in first_result.lower(), \
        f"Expected '{search_term}' in results but got '{first_result}'"

    logger.info(f"✅ Search successful for: {search_term}")
