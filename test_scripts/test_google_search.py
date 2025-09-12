from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Automation Testing with Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    print("Page title is:", driver.title)
    driver.quit()

if __name__ == "__main__":
    test_google_search()
