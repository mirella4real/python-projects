#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import pprint
from data_manager import DataManager

flight_data = DataManager()
sheet_data = flight_data.get_worksheet_data()
pprint.pprint(sheet_data)