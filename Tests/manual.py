from ProcessData.WaitroseProcessHTML import *
from ProcessData.TescoProcessHTML import *
from RetrieveData.RetrieveData import *

print("started")
url = "https://www.tesco.com/groceries/en-GB/search?query=" + "milk"
content = RetrieveDataAt(url)
print(content)