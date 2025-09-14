from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_result_text(self):
        # Wait until the first result link is visible
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.result__a"))
        )
        return result.text
