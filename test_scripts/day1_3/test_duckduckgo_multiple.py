import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("query", [
    "Automation Testing with Selenium",
    "DevOps Roadmap 2025",
    "Python pytest tutorial"
])
def test_duckduckgo_search(driver, query):
    driver.get("https://duckduckgo.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    # ✅ Check if query appears in title
    assert query in driver.title
