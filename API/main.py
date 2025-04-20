#API
import pytest
import requests
import json
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from RetrieveData.RetrieveData import *

from ProcessData.WaitroseProcessHTML import *
from ProcessData.TescoProcessHTML import *

from API.DataValidation import *

#Data formatting
from pydantic import BaseModel
from typing import List

#For async operations
import asyncio

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class SearchModel(BaseModel):
    keyword: str
    supermarkets: List[str]
    filter: str

class LocationModel(BaseModel):
    location: str

@app.post("/api/test")
async def test():
    print("reached")
    return {"result": "worked"}

@app.get("/api/supermarketSearchByLocation")
async def supermarketSearchByLocation(locationModel: LocationModel):
    headers = {
        "accept": "application/json",
        "Authorization": "bearer 0iJ6q77vDLoWeOod_0VRej8bNBLpEG-T79vNoDkhY0DM_PtcVEveTm6alZ0LtrHJ_476_JPhbPC1JtZbHn_kJLwe0NgReB-ouuB-sxE5bIC_6_-cvlmhSZgJOSSMZHYx"
    }

    supermarkets = ["Waitrose", "Tesco", "Asda"]
    data = []

    for supermarket in supermarkets:
        url = f'https://api.yelp.com/v3/businesses/search?location={locationModel.location}&term={supermarket}&radius=5000&sort_by=best_match&limit=1'
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and ValidateSupermarketLocation(supermarket, json.loads(response.text)["businesses"]):
            data.append(json.loads(response.text)["businesses"])

    return data

@app.post("/api/search")
async def Search(searchModel: SearchModel):
    print("search")
    filter_mapping = {
        ("tesco", "Best value"): TescoFindBestValue,
        ("tesco", "Least expensive"): TescoFindCheapest,
        ("waitrose", "Least expensive") : WaitroseFindCheapest,
        ("waitrose", "Best value") : WaitroseFindBestValue
    }

    coroutines = [filter_mapping[(supermarket, searchModel.filter)](searchModel.keyword) for supermarket in searchModel.supermarkets]

    results = await asyncio.gather(*coroutines)

    return results

# Waitrose

async def WaitroseFindCheapest(keyword):
    url = "https://www.waitrose.com/ecom/shop/search?ct=" + str(keyword) + "&searchTerm=" + str(keyword) + "&sortBy=PRICE_LOW_2_HIGH"
    content = RetrieveDataAt(url)
    waitrose = WaitroseProcessHTML(content)
    return waitrose.waitroseGetFirstItem()

async def WaitroseFindBestValue(keyword):
    url = "https://www.waitrose.com/ecom/shop/search?ct=" + str(keyword) + "&searchTerm=" + str(keyword)
    content = RetrieveDataAt(url)
    waitrose = WaitroseProcessHTML(content)
    return waitrose.waitroseBestValue()

# Tesco

async def TescoFindCheapest(keyword):
    url = "https://www.tesco.com/groceries/en-GB/search?query=" + str(keyword) + "&count=10&sortBy=price-ascending"
    content = RetrieveDataAt(url)
    tesco = TescoProcessHTML(content)
    return tesco.tescoGetFirst()

async def TescoFindBestValue(keyword):
    url = "https://www.tesco.com/groceries/en-GB/search?query=" + str(keyword) + "&page=1&count=10"
    content = RetrieveDataAt(url)
    tesco = TescoProcessHTML(content)
    return tesco.tescoBestValue()

