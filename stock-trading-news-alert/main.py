from config import *
from test_data import *
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
def compute_percentage_difference(final:float, initial:float)->float:
    percentage_change = (final-initial)/initial * 100
    return percentage_change

def get_stock_data():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_KEY
    }
    if IS_TEST:
        stock_data = ALPHAVANTAGE_MOCK_DATA
    else:
        stock_data = call_api(ALPHAVANTAGE_ENDPOINT, parameters)
    return stock_data

def get_closing_status(stock_data)->dict:
    closing_status = {
        "status": "Same",
        "difference": 0
    }
    daily_keys = list(stock_data["Time Series (Daily)"].keys())
    today_close = float(stock_data["Time Series (Daily)"][daily_keys[0]]['4. close'])
    yesterday_close = float(stock_data["Time Series (Daily)"][daily_keys[1]]['4. close'])
    closing_status["difference"] = compute_percentage_difference(today_close, yesterday_close)
    if today_close > yesterday_close:
        closing_status["status"] = "Increase"
    elif yesterday_close > today_close:
        closing_status["status"] = "Decrease"
    return closing_status


stock_data = get_stock_data()
closing_status = get_closing_status(stock_data)
if closing_status["difference"] >= 5:
    print("Good news!")
    
