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

def test_google_search(driver):
    driver.get("https://duckduckgo.com/")

    # Search box by NAME attribute
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Automation Testing with Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(6)
    assert "Automation Testing with Selenium" in driver.title