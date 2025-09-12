import pytest
from selenium import webdriver
from test_scripts.day4.pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Check if redirected to products page
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.enter_username("wrong_user")
    login_page.enter_password("wrong_pass")
    login_page.click_login()

    # Check error message
    assert "Username and password do not match" in login_page.get_error_message()
