import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from ProcessData.Driver import *

class AsdaProcessHTML:
    def __init__(self, url):
        self.url = url
        self.driver = CreateDriver()
        self.soupExtracted = self.GetExtractedSoup()

    def GetExtractedSoup(self):
        OpenDriverAt(self.url, self.driver)

        # Retrieve the HTML source code
        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")

        #There are many irrelevant items on the page (suggested items etc)
        #This is the container which holds the relevant ones
        ul = soup.find('ul', class_='co-product-list__main-cntr co-product-list__main-cntr--rest-in-shelf')

        # Find all 'li' elements within the 'ul'
        li_elements = ul.find_all('li')

        soupExtracted = BeautifulSoup(str(li_elements), 'html.parser', from_encoding="utf-8")

        return soupExtracted

    def AsdaGetNames(self):
        """
        Opens the given asda url and gets the names of all relevant items (The asda site shows suggested items which
        make searching ambigous)
        :param url: The asda url which will take selenium to the asda page
        :return: An array of string of the names of the items from the page e.g "Semi Skimmed milk", "Dairy Milk" ...
        """
        a_elements = self.soupExtracted.find_all("a", class_="co-product__anchor")
        a_elements_text = [a.text for a in a_elements]

        return a_elements_text

    def AsdaGetMeasurements(self):
        """
        Opens the given asda url and gets the names of all relevant items (The asda site shows suggested items which
        make searching ambigous)
        :param url: The asda url which will take selenium to the asda page
        :return: An array of string of the measurements for the given items from the page e.g "4 pints", "400 grams" ...
        """
        span_elements = self.soupExtracted.find_all("span", class_="co-product__volume co-item__volume")
        span_elements_text = [s.text.strip() for s in span_elements]

        return span_elements_text

    def AsdaGetImages(self, names):
        """
        Gets the images for all the 'names' of products
        :param names: an array of names e.g '4 pint milk'
        :return: an array of urls to all the respective images
        """
        def SearchForImage(name):
            image_element = self.driver.find_element('css selector', f'img[alt="{name}"]')
            return image_element

        images = []
        for name in names:
            notFound = True
            while(notFound):
                try:
                    image = SearchForImage(name)
                    images.append(image.get_attribute("src"))
                    notFound = False
                except NoSuchElementException:
                    print("not found")


        return images


