from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")   # run without opening browser (optional)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
