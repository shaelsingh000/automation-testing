import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import logger   # Import the singleton logger


@pytest.fixture
def driver():
    """Fixture to initialize and quit Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver  # Test runs here

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results and take screenshots on failure."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}_failure.png"
            driver.save_screenshot(screenshot_path)
            logger.error(f"❌ Test {item.name} failed. Screenshot saved at {screenshot_path}")

            # Attach to pytest-html report if plugin is enabled
            if hasattr(rep, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    rep.extra.append(pytest_html.extras.image(screenshot_path))
