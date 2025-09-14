from selenium.webdriver.common.by import By

class DuckDuckGoResultsPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def __init__(self, driver):
        self.driver = driver

    def results(self):
        return self.driver.find_elements(*self.RESULT_LINKS)

    def first_result_text(self):
        return self.results()[0].text if self.results() else None
