# file to hold credentials 

import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

# Constants
STATION_CODE = "D07"
WMATA_API_KEY = os.getenv("WMATA_API_KEY")

# Validate
assert WMATA_API_KEY, "WMATA_API_KEY not found in environment."
