from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultsPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def __init__(self, driver):
        self.driver = driver

    def get_first_result_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.RESULT_LINKS)
        )
        return self.driver.find_elements(*self.RESULT_LINKS)[0].text
