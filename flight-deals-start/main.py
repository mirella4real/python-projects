#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import pprint
from data_manager import DataManager
from flight_search import FlightSearch

flight_data = DataManager()
flight_search = FlightSearch()

def update_iata_codes(cities_list:list):
    updated_cities_list = []
    for city in cities_list:
        if len(city["iataCode"]) == 0:
            iata_code = flight_search.get_iata_code(city["city"])
            city["iataCode"] = iata_code
        updated_cities_list.append(city)
    return updated_cities_list
        

sheet_data = flight_data.get_worksheet_data()
sheet_data = update_iata_codes(sheet_data)
pprint.pprint(sheet_data)

update_iata_codes(sheet_data)

