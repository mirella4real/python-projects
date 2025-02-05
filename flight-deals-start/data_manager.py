from config import *
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_worksheet_data(self):
        try:
            response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADER)
            response.raise_for_status() 
            data = response.json()
            return data["prices"]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    

