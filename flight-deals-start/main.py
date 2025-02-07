#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import pprint
from data_manager import DataManager
from flight_search import FlightSearch

flight_data = DataManager()
flight_search = FlightSearch()

def search_flights(cities_list:list):
    for city in cities_list:
        if len(city["iataCode"]) == 0:
            print(flight_search.get_iata_code(city["city"]))

sheet_data = flight_data.get_worksheet_data()
search_flights(sheet_data)

