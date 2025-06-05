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


def get_trains(STATION_CODE = STATION_CODE, line_filter = 'SV'):
    """
    Parses a response object from the WMATA API. 
    Args: 
    STATION_CODE: Station code of the station you want. 
    line: Line. Defaults to 'SV' for Silver Line trains. Enter None or 'any' for the next three trains. 
    Possible lines are 'OR','BL','SV', 'YL','GR'
    """
    url = f'http://api.wmata.com/StationPrediction.svc/json/GetPrediction/{STATION_CODE}' #wmata train prediction url
    headers = {'api_key': API_KEY}
    line_filter = line_filter.lower()
    # handle errors 
    try: 
        response = requests.get(url, headers=headers, timeout= 5)
        response.raise_for_status()
    except requests.RequestException() as e: 
        print(f'Error fetching train data: {e}')
    data = response.json().get('Trains', [])
    trains = data['Trains']
    # filter for silver line trains
    if line_filter != 'any': 
        trains = [t for t in trains if t["Line"] == line_filter] # Silver line only 
    else: 
        trains = trains[:3] # next three trains 
    return trains 

def format_train_data(trains): 
    #TODO 