from config import *
from test_data import *
from datetime import datetime
import requests
IS_TEST = True
STOCK = "IBM"
COMPANY_NAME = "International Business Machines (IBM)"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

def call_api(api_url, parameters=None):
    if parameters != None:
        response = requests.get(url=api_url, params=parameters)
    else:
        response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY
}

if IS_TEST:
    stock_data = ALPHAVANTAGE_MOCK_DATA
else:
    stock_data = call_api(ALPHAVANTAGE_ENDPOINT, parameters)

print(stock_data)
    
