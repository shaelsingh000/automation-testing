import pytest
from test_scripts.day12.pages.duckduckgo_home import DuckDuckGoHomePage
from test_scripts.day12.pages.duckduckgo_result import DuckDuckGoResultsPage

search_term = ["Selenium Python", "Pytest Tutorial", "Automation Testing"]

@pytest.mark.parametrize("term", search_term)
def test_duckduckgo_search(driver, term):
    home = DuckDuckGoHomePage(driver)
    home.load()
    home.search(term)
    results = DuckDuckGoResultsPage(driver)
    first_result_text = results.get_first_result_text()
    assert term.split()[0].lower() in first_result_text.lower()
