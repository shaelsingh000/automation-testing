import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.logger import get_logger
from datetime import datetime
import allure

logger = get_logger("pytest")

@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Capture screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}_failure.png"
            driver.save_screenshot(screenshot_path)
            logger.error(f"❌ Test {item.name} failed. Screenshot saved at {screenshot_path}")

            # Attach to pytest-html
            if hasattr(rep, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    rep.extra.append(pytest_html.extras.image(screenshot_path))

            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name=f"{item.name}_screenshot",
                              attachment_type=allure.attachment_type.PNG)
