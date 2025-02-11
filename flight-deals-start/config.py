import os
from dotenv import load_dotenv

IS_TEST = True

def init_config():
    load_dotenv("./.venv/.env")

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





