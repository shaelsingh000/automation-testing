from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure

class DuckDuckGoPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")        # Usually the search input uses name="q"# Might still work; inspect
    SEARCH_RESULTS = (By.CSS_SELECTOR, "a.result__a")

    @allure.step("Open DuckDuckGo homepage")
    def open_homepage(self):
        self.open("https://duckduckgo.com/")

    @allure.step("Search for term: {term}")
    def search(self, term):
        self.type(*self.SEARCH_INPUT, text=term)
        self.find(self.SEARCH_INPUT).send_keys(Keys.RETURN) 
    
    @allure.step("Get search results for validation")
    def get_results(self):
        elements = self.wait_all(self.SEARCH_RESULTS)
        return [elem.text for elem in elements]
