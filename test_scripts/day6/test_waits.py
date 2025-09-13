import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_implicit_wait(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()

    # Explicit wait needed because element exists but is hidden
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

    assert "Hello World!" in element.text


def test_explicit_wait(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()
    # Explicit wait for the element to be visible
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert "Hello World!" in element.text