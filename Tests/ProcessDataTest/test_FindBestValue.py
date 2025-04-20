import pytest
from ProcessData.FindBestValue import *

@pytest.mark.parametrize("data, expected", [
    ([{"name": "milk", "price": "£1.50/each", "img": ""}, {"name": "banana", "price": "£0.50/each", "img": ""},
            {"name": "chocolate milk", "price": "£0.25/litre", "img": ""}], {"name": "banana", "price": "£0.50/each", "img": ""})
])
def test_TescoFindBestValue(data, expected):
    actual = TescoFindBestValue(data)
    assert actual == expected

@pytest.mark.parametrize("data, expected", [
    ([{"name": "milk", "price": "£1.50", "value": "£1.50/each", "img": ""}, {"name": "banana", "price": "£1.50", "value": "50p/each", "img": ""},
            {"name": "chocolate milk", "price": "£1.50", "value": "£0.25/litre", "img": ""}], {"name": "banana", "price": "£1.50", "value": "£0.50/each", "img": ""})
])
def test_WaitroseFindBestValue(data, expected):
    actual = WaitroseFindBestValue(data)
    print(actual)
    assert actual == expected