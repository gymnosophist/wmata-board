from wmata.config import WMATA_API_KEY, STATION_CODE
from wmata.render import render_trains 
from wmata.trains import get_trains #, display_trains 
import os 
import requests
import argparse 
from dotenv import load_dotenv



load_dotenv()

API_KEY=os.getenv("WMATA_API_KEY")

STATION_CODE = 'D07'
line_filter = 'SV'
def main(): 
    # parse arguments 
    parser =  argparse.ArgumentParser() 

    parser.add_argument(
        "-l", "--line", 
        type=str, 
        default='SV',
        help="Filter for train line, e.g. SV, BL, OR, etc. Defaults to SV" 
    )
    
    parser.add_argument(
        "-s", "--station", 
        type=str, 
        default="D07",
        help="Select a station. Defaults to D07, Potomac Ave. See list of stations here: https://gist.github.com/emma-k-alexandra/72d2a19e3ebd280e9640f4414f063d6b"

    )
    
    # add args 
    args = parser.parse_args()
    # get train data 
    trains = get_trains(STATION_CODE=args.station, line_filter=args.line)
    if trains:
        print('got trains')
    else:
        print('error getting trains')
    #change this to render trains 
    # display_trains(trains)

    
if __name__ == "__main__":
    main()
