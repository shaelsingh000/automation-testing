import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to fetch test data from CSV
def get_search_data():
    with open("test_scripts/day7/search_data.csv") as f:
        reader = csv.DictReader(f)
        return [row["query"] for row in reader]

# Fixture to initialize and quit browser
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Parametrize test using CSV data
@pytest.mark.parametrize("search_term", get_search_data())
def test_duckduckgo_search(driver, search_term):
    driver.get("https://duckduckgo.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Wait until at least one result link is visible
    wait = WebDriverWait(driver, 10)
    results = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    # Ensure we got results
    assert len(results) > 0

    # Check that at least one result contains the search term
    assert any(search_term.lower() in r.text.lower() for r in results)
