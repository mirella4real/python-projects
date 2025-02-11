import os
import requests
import pprint
from dotenv import load_dotenv

IS_TEST = True

def init_config():
    load_dotenv("./.venv/.env")

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
    pprint.pprint(response.json())

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





