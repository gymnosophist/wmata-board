import os 
import requests

API_KEY=os.getenv("WMATA_API_KEY")
STATION_CODE = "D07" #potomac ave 

url = f'http://api.wmata.com/StationPrediction.svc/json/GetPrediction/{STATION_CODE}'
headers = {'api_key': API_KEY}

response = requests.get(url, headers=headers)
data = response.json()

print(data)