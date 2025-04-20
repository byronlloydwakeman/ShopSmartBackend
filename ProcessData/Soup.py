from bs4 import BeautifulSoup
from ProcessData.Driver import *

def createSoup(file_content):
    soup = BeautifulSoup(file_content, 'html.parser', from_encoding="utf-8")
    return soup

def createSoupAt(url):
    driver = CreateDriver()

    OpenDriverAt(url, driver)

    # Retrieve the HTML source code
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

    return soup
