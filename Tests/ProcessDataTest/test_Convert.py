import pytest
from ProcessData.Convert import *

@pytest.mark.parametrize("data, expected", [
    ([{"name": "milk", "price": "£1.33", "image": "", "value" : '£2.10/litre'}, {"name": "milk", "price": "£1.33", "image": "", "value" : "50p/litre"}],
        [{"name": "milk", "price": "£1.33", "image": "", "value" : '£2.10/litre'}, {"name": "milk", "price": "£1.33", "image": "", "value": '£0.50/litre'}])
])
def test_createSoupAtContains(data, expected):
    values = PenceToPound(data)
    print(values)
    assert values == expected