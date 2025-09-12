import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"
    dropdown.select_by_index(2)
    assert dropdown.first_selected_option.text == "Option 2"

def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    if not checkboxes[0].is_selected():
        checkboxes[0].click()
    if checkboxes[1].is_selected():
        checkboxes[1].click()
    assert checkboxes[0].is_selected()
    assert not checkboxes[1].is_selected()

def test_input_box(driver):
    driver.get("https://the-internet.herokuapp.com/inputs")
    input_box = driver.find_element(By.TAG_NAME, "input")
    input_box.send_keys("12345")
    assert input_box.get_attribute("value") == "12345"

def test_alerts(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click "JS Alert"
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert "I am a JS Alert" in alert.text
    alert.accept()

    # JS Confirm
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm = driver.switch_to.alert
    confirm.dismiss()
    assert "You clicked: Cancel" in driver.find_element(By.ID, "result").text

def test_screenshot(driver):
    driver.get("https://the-internet.herokuapp.com/")
    driver.save_screenshot("day5/homepage.png")