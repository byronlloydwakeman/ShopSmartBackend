from bs4 import BeautifulSoup
from ProcessData.WaitroseProcessHTML import WaitroseProcessHTML
from RetrieveData.RetrieveData import *
import pytest

content = RetrieveDataAt("https://www.waitrose.com/ecom/shop/search?&searchTerm=milk", )

waitroseInstanceWithoutAPI = WaitroseProcessHTML(content)

@pytest.mark.parametrize("expectedData", [
    (50)
])
def test_waitroseGetNames(expectedData):
    names = waitroseInstanceWithoutAPI.waitroseGetNames()
    print(names)
    assert len(names) == expectedData

@pytest.mark.parametrize("expectedData", [
    (50)
])
def test_waitroseGetPrices(expectedData):
    prices = waitroseInstanceWithoutAPI.waitroseGetPrices()
    print(prices)
    assert len(prices) == expectedData

@pytest.mark.parametrize("expectedData", [
    (50)
])
def test_waitroseGetImages(expectedData):
    images = waitroseInstanceWithoutAPI.waitroseGetImages()
    print(images)
    assert len(images) == expectedData

@pytest.mark.parametrize("expectedData", [
    (50)
])
def test_processWaitroseHtml(expectedData):
    result = waitroseInstanceWithoutAPI.processWaitroseHtml()
    print(result)
    assert len(result) == expectedData

@pytest.mark.parametrize("expected", [
    (47)
])
def test_watiroseGetValues(expected):
    result = waitroseInstanceWithoutAPI.waitroseGetValues()
    print(result)
    assert len(result) == expecteduu

@pytest.mark.parametrize("data, expected", [
    ([{"name": "milk", "price": "£1.33", "image": "", "value" : 'Price per unit£2.10/litre'}, {"name": "milk", "price": "£1.33", "image": "", "value" : 'Price per unit£1.33/litre'}],
        [{"name": "milk", "price": "£1.33", "image": "", "value" : '£2.10/litre'}, {"name": "milk", "price": "£1.33", "image": "", "value": '£1.33/litre'}])
])
def test_waitroseCleanValues(data, expected):
    result = waitroseInstanceWithoutAPI.waitroseCleanValues(data)
    print(result)
    assert result == expected


