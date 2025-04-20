import pytest
import time
from ProcessData.Driver import *

@pytest.mark.parametrize("url, data", [
    ("https://groceries.asda.com/search/milk", "Cow & Gate 3 Growing Up Milk 15 Pack"),
    ("https://groceries.asda.com/search/milk", "ASDA Semi Skimmed Milk")
])
def test_GetImages(url, data):
    driver = CreateDriver()
    OpenDriverAt(url, driver)
    print(data)
    image_element = driver.find_element('css selector', f'img[alt="{data}"]')
    print("image" + image_element.get_attribute("src"))
    assert False
