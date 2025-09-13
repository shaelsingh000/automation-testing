import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to fetch test data from Excel
def get_search_data():
    workbook = openpyxl.load_workbook("test_scripts/day8/search_data.xlsx")
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
        data.append(row[0])
    return data

# Fixture for driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Parametrize test with Excel data
@pytest.mark.parametrize("search_term", get_search_data())
def test_duckduckgo_search_excel(driver, search_term):
    driver.get("https://duckduckgo.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results
    wait = WebDriverWait(driver, 10)
    results = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    # Assert at least one result contains the search term
    assert any(search_term.lower() in r.text.lower() for r in results)
