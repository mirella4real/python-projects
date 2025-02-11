from config import *

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = get_amadeus_api_key()
        self._api_secret = get_amadeus_api_secret()
        self._api_token = get_amadeus_api_token()

    def get_iata_code(self, city:str)->str:
        return "TESTING"