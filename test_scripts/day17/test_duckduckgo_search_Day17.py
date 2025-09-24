import pytest
from utils.logger import get_logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

logger = get_logger()

@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  # optional
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

search_terms = ["Selenium Python", "Pytest Tutorial", "Automation Testing"] 

@pytest.mark.parametrize("search_term", search_terms)
def test_duckduckgo_search(driver, search_term):
    logger.info(f"Starting test with search term: {search_term}")


    driver.get("https://duckduckgo.com/")
    logger.info("Opened DuckDuckGo")

    search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchbox_input"))
)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    logger.info(f"Searching for: {search_term}")

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )

    results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    assert results, f"No results found for {search_term}"

    first_result = results[0].text
    logger.info(f"First result text: {first_result}")

    assert search_term.split()[0].lower() in first_result.lower(), \
        f"Expected '{search_term}' in '{first_result}'"