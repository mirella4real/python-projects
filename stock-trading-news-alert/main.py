from config import *
import requests
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
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": ALPHAVANTAGE_KEY
}
stock_data = call_api(ALPHAVANTAGE_ENDPOINT, parameters)
print(stock_data)