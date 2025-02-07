from config import *
import requests

TEST_DATA = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
 {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
 {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
 {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_worksheet_data(self):
        if IS_TEST != True:
            try:
                response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADER)
                response.raise_for_status() 
                data = response.json()
                return data["prices"]
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None
        else:
            return TEST_DATA
    

