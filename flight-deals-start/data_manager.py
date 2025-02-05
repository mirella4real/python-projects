from config import *
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_worksheet_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADER)
        return response.json()

