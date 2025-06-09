from render import render_trains

mock_trains = [
    {"Line": "SV", "Car": "6", "Destination": "Wiehle", "Min": "2"},
    {"Line": "SV", "Car": "8", "Destination": "Ashburn", "Min": "6"},
    {"Line": "SV", "Car": "6", "Destination": "Largo", "Min": "BRD"},
]

render_trains(mock_trains)