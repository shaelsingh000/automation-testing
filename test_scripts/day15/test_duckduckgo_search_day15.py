import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("search_term", [
    "Selenium Python",
    "Pytest Tutorial",
    "Automation Testing"
])
def test_duckduckgo_search(search_term):
    logger.info(f"Starting test with search term: {search_term}")

    # Setup Chrome in headless mode
    chrome_options = Options()
    #chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://duckduckgo.com/")
        logger.info("Opened DuckDuckGo")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        logger.info(f"Searching for: {search_term}")

        # Wait until results load
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
        )


        results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
        assert results, "No search results found!"
        logger.info(f"Found {len(results)} results")

        first_result_text = results[0].text
        logger.info(f"First result text: {first_result_text}")

        # Assert search term is in first result
        assert any(word.lower() in first_result_text.lower() for word in search_term.split()), \
            f"'{search_term}' not found in first result: {first_result_text}"

        logger.info(f"Test passed for {search_term}")

    except Exception as e:
        logger.error(f"Test failed for {search_term} - Error: {str(e)}")
        raise
    finally:
        driver.quit()
