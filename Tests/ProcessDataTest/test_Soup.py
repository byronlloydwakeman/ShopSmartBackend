from ProcessData.Soup import *
import pytest

@pytest.mark.parametrize("url, data", [
    ("https://groceries.asda.com/search/milk", "Cow & Gate 3 Baby Toddler Milk Formula 1+ Years")
])
def test_createSoupAtContains(url, data):
    soup = createSoupAt(url)
    print(str(soup))
    if data in str(soup):
        assert True
    else:
        assert False