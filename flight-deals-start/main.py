#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from config import *
import requests

def get_worksheet_data():
    response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADER)
    return response.json()

print(get_worksheet_data())