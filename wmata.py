# utility functions 

def format_trains(trains, max_lines=3, max_dest_len=10):
    """
    Parses a response object from the WMATA API. 
    """
    trains = [t for t in trains if t["Line"] == 'SV'] # Silver line only 
    for train in trains[:max_dest_len]:
        line=trains["Line"]

