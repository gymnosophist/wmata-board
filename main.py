from wmata.config import WMATA_API_KEY, STATION_CODE
from wmata.render import render_trains 
from wmata.trains import get_trains #, display_trains 
import argparse 

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

    parser.add_argument(
        "-t", "--test",
        action="store_true"
        help = "Print train data to console without rendering"

    )
    
    # add args 
    args = parser.parse_args()
    # get train data 
    trains = get_trains(STATION_CODE=args.station, line_filter=args.line)
    if trains:
        print('got trains')
    else:
        print('error getting trains')
    if args.test:
        for t in trains: 
            print(t)
    else:
        render_trains(trains)

    
if __name__ == "__main__":
    main()
