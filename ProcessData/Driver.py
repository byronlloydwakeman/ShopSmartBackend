import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def CreateDriver():
    # Set the path to the ChromeDriver executable
    chromedriver_path = 'C:/Users/44785/PycharmProjects/ShopSmart/WebDriver/chromedriver_win32/chromedriver.exe'

    # Configure Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode without opening a browser window

    # Create a new Chrome driver instance
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    return driver

def OpenDriverAt(url, driver):
    # Navigate to the desired webpage
    driver.get(url)

    # Wait for the dynamic content to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

    try:
        # Theres a terms and conditions pop-up, this just closes it
        button = driver.find_element(by='id', value='onetrust-accept-btn-handler')
        button.click()
    except NoSuchElementException:
        pass

    time.sleep(5)
