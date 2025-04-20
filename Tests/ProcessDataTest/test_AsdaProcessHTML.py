import pytest
from ProcessData.AsdaProcessHTML import AsdaProcessHTML

asdaInstance = AsdaProcessHTML("https://groceries.asda.com/search/milk")

@pytest.mark.parametrize("data", [
    ("ASDA Semi Skimmed Milk")
])
def test_getExtractedSoupContains(data):
    extractedSoup = asdaInstance.GetExtractedSoup()
    print(extractedSoup)
    if data in str(extractedSoup):
        assert True
    else:
        assert False

@pytest.mark.parametrize("expectedData", [
    (59)
])
def test_asdaGetNames(expectedData):
    names = asdaInstance.AsdaGetNames()

    assert len(names) == expectedData

@pytest.mark.parametrize("expectedData", [
    (59)
])
def test_asdaGetMeasurements(expectedData):
    measurements = asdaInstance.AsdaGetMeasurements()
    print(measurements)
    assert len(measurements) == expectedData

@pytest.mark.parametrize("expectedData", [
    (59)
])
def test_asdaGetImages(expectedData):
    images = asdaInstance.AsdaGetImages(asdaInstance.AsdaGetNames())
    print(images)
    assert len(images) == expectedData

@pytest.mark.parametrize("data, expectedData", [
    (["ASDA Semi Skimmed Milk"], 1),
    (["ASDA Long Life Skimmed Milk"], 1),
])
def test_asdaGetImage(data, expectedData):
    images = asdaInstance.AsdaGetImages(data)
    print(data)
    assert len(images) == expectedData