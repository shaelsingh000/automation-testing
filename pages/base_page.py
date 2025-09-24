import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def open(self, url):
        with allure.step(f"Open URL: {url}"):
            self.driver.get(url)
            self._attach_screenshot("open_url")

    def find(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def click(self, locator, step_desc=None):
        step_desc = step_desc or f"Click element {locator}"
        with allure.step(step_desc):
            try:
                element = self.find(locator)
                element.click()
                self._attach_screenshot(f"click_{locator[1]}")
            except Exception as e:
                self._attach_screenshot(f"click_failed_{locator[1]}")
                raise e

    def type(self, by, locator, text):
        with allure.step(f"Type '{text}' into {locator}"):
            element = self.find((by, locator))
            element.clear()
            element.send_keys(text)
            self._attach_screenshot(f"type_{locator}")

    def wait_all(self, locator, timeout=None):
        """Wait until all elements matching locator are present"""
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_elements(*locator)  # note find_elements, not find_element
        )

    def _attach_screenshot(self, name):
        # Attach screenshot to Allure
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=allure.attachment_type.PNG)
