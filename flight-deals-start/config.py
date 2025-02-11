import os
import requests
import pprint
from dotenv import load_dotenv

IS_TEST = True

def init_config():
    load_dotenv("./.venv/.env")
    get_new_token()

def get_new_token():
    header = {
        'Content-type': 'application/x-www-form-urlencoded'
    }
    body = {
        'grant_type': 'client_credentials',
        'client_id': get_amadeus_api_key(),
        'client_secret': get_amadeus_api_secret()
    }
    response = requests.post(url=os.getenv("AMADEU_API_OAUTH2"), headers=header, data=body)
    access_token = response.json()['access_token']
    os.putenv(access_token, "AMADEUS_API_TOKEN")

def get_sheety_endpoint():
    return os.getenv("SHEETY_API_ENDPOINT")

def get_sheety_header():
    return{ "Authorization": os.getenv("SHEETY_TOKEN")}

def get_amadeus_endpoint():
    return os.getenv("AMADEUS_API_ENDPOINT")

def get_amadeus_api_key():
    return os.getenv("AMADEUS_API_KEY")

def get_amadeus_api_secret():
    return os.getenv("AMADEUS_API_SECRET")

def get_amadeus_api_token():
    return os.getenv("AMADEUS_API_TOKEN")


SAVED_TEST_DATA = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
 {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
 {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
 {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]


