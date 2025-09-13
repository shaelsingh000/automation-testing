from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoHomePage:
    URL = "https://duckduckgo.com/"
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, term):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)
