import pprint
from config import init_config
from data_manager import DataManager
from flight_search import FlightSearch

flight_data = DataManager()
flight_search = FlightSearch()

def update_iata_codes(cities_list:list):
    updated_cities_list = []
    for city in cities_list:
        if not city["iataCode"]:
            city["iataCode"] = flight_search.get_iata_code(city["city"])
        updated_cities_list.append(city)
    return updated_cities_list

init_config()        
sheet_data = flight_data.get_worksheet_data()
sheet_data = update_iata_codes(sheet_data)
flight_data.update_worksheet(sheet_data)

