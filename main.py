from wmata.trains import get_trains, display_trains 
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("WMATA_API_KEY")

STATION_CODE = 'D07'
line_filter = 'SV'
def main(): 
    trains = get_trains(STATION_CODE=STATION_CODE, line_filter='SV')
    if trains:
        print('got trains')
    else:
        print('error getting trains')
    display_trains(trains)
    
if __name__ == "__main__":
    main()
