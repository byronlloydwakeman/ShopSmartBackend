from RetrieveData.RetrieveData import *

@pytest.mark.parametrize("url", [
    ("https://www.waitrose.com/ecom/shop/search?&searchTerm=milk"),
    ("https://www.tesco.com/groceries/en-GB/search?query=milk")
])
def test_RetrieveDataAt(url):
    content = RetrieveDataAt(url)
    print(content)
    assert len(content) != 0
