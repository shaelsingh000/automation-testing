from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DuckDuckGoPage(BasePage):
    URL = "https://duckduckgo.com/"

    SEARCH_INPUT = (By.ID, "searchbox_input")  # verify in browser
    RESULT_LINKS = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def load(self):
        self.open(self.URL)

    def search(self, term):
        self.type(*self.SEARCH_INPUT, text=term)
        self.driver.find_element(*self.SEARCH_INPUT).submit()

    def get_first_result(self):
        return self.wait(self.RESULT_LINKS)
