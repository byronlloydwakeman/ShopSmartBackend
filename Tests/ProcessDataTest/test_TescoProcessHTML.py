import pytest
from bs4 import BeautifulSoup
from ProcessData.TescoProcessHTML import *
from RetrieveData.RetrieveData import *

@pytest.mark.parametrize("expected", [
    (2)
])
def test_FindNumberOfSponsoredItems(expected):
    file_path = 'C:/Users/44785/PycharmProjects/ShopSmart/Tests/ProcessDataTest/TestData/tescoTestData.html'
    file_content = ''

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, 'html.parser', from_encoding="utsf-8")

    number = findNumberOfSponsoredItems(soup)

    assert number == expected

@pytest.mark.parametrize("expectedData", [
    (26)
])
def test_TescoGetNames(expectedData):
    file_path = 'C:/Users/44785/PycharmProjects/ShopSmart/Tests/ProcessDataTest/TestData/tescoTestData.html'
    file_content = ''

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, 'html.parser', from_encoding="utf-8")
    names = tescoGetNames(soup)
    print(names)
    assert len(names) == expectedData

@pytest.mark.parametrize("expectedData", [
    (26)
])
def test_TescoGetPrices(expectedData):
    file_path = 'C:/Users/44785/PycharmProjects/ShopSmart/Tests/ProcessDataTest/TestData/tescoTestData.html'
    file_content = ''

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, 'html.parser', from_encoding="utf-8")
    prices = tescoGetPrices(soup)
    print(prices)
    assert len(prices) == expectedData

@pytest.mark.parametrize("expectedData", [
    (26)
])
def test_TescoGetImages(expectedData):
    file_path = 'C:/Users/44785/PycharmProjects/ShopSmart/Tests/ProcessDataTest/TestData/tescoTestData.html'
    file_content = ''

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, 'html.parser', from_encoding="utf-8")
    images = tescoGetImages(soup)
    print(images)
    assert len(images) == expectedData

@pytest.mark.parametrize("data", [
    ("milk")
])
def test_TescoGetValues(data):
    url = "https://www.tesco.com/groceries/en-GB/search?query=" + data
    content = RetrieveDataAt(url)

    tesco = TescoProcessHTML(content)
    actual = tesco.tescoGetValues()
    print(actual)
    assert len(actual) != 0

@pytest.mark.parametrize("data", [
    ("milk")
])
def test_TescoBestValue(data):
    url = "https://www.tesco.com/groceries/en-GB/search?query=" + data
    content = RetrieveDataAt(url)

    tesco = TescoProcessHTML(content)
    actual = tesco.tescoBestValue()
    print(actual)
    assert True


@pytest.mark.parametrize("data, expected", [
    ("milk", "Tesco British Semi Skimmed Milk 2.272L 4 Pints")
])
def test_TescoProcessHtml(data, expected):
    url = "https://www.tesco.com/groceries/en-GB/search?query=" + data
    content = RetrieveDataAt(url)

    tesco = TescoProcessHTML(content)
    actual = tesco.tescoGetFirst()
    print(actual)
    assert actual["name"] == expected