#API
import pytest
import requests
import json
import uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Accept": "text/html",
    "Accept-Encoding": "gzip, deflate, br"
}

def RetrieveDataAt(url):
    # Send a GET request to the API endpoint
    response = requests.get(url, headers=headers)
    return response.text.replace("&quot;", '"')

