import pytest
from pages.duckduckgo_page import DuckDuckGoPage
from utils.logger import get_logger
from utils.data_reader import read_csv,read_json,read_yaml

logger = get_logger()

search_terms = read_json("search_terms.json")  # Can swap with JSON/YAML reader

@pytest.mark.parametrize("search_term", search_terms)
def test_duckduckgo_search(driver, search_term):
    logger.info(f"Starting test with search term: {search_term}")

    duckduckgo = DuckDuckGoPage(driver)
    duckduckgo.load()
    logger.info("Opened DuckDuckGo")

    duckduckgo.search(search_term)
    logger.info(f"Searching for: {search_term}")

    assert search_term.lower() in driver.page_source.lower()
    logger.info(f"✅ Search successful for: {search_term}")
