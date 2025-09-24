import pytest
import json
import logging
from test_scripts.day14.pages.duckduckgo_home import DuckDuckGoHomePage
from test_scripts.day14.pages.duckduckgo_result import DuckDuckGoResultsPage

# Load search terms from JSON
def load_test_data():
    with open("test_scripts/day14/test_data.json") as f:
        data = json.load(f)
    return data["search_terms"]

@pytest.mark.parametrize("term", load_test_data())
def test_duckduckgo_search(driver, term):
    logging.info(f"Running search test for: {term}")

    home = DuckDuckGoHomePage(driver)
    home.load()
    home.search(term)

    results = DuckDuckGoResultsPage(driver)
    first_result = results.get_first_result_text()

    logging.info(f"First result text: {first_result}")
    assert term.split()[0].lower() in first_result.lower()
