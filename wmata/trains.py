# utility functions 

import os 
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("WMATA_API_KEY")

# check for API key 
assert WMATA_API_KEY, "WMATA_API_KEY not found in environment."

STATION_CODE = "D07" #potomac ave 
# we can put this in the function 


def get_trains(STATION_CODE = STATION_CODE):
    """
    Parses a response object from the WMATA API. 
    """
    url = f'http://api.wmata.com/StationPrediction.svc/json/GetPrediction/{STATION_CODE}'
    headers = {'api_key': API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    trains = data['Trains']
    # filter for silver line trains 
    trains = [t for t in trains if t["Line"] == 'SV'] # Silver line only 
    

train_data = get_trains()

def format_train_data(trains): 
