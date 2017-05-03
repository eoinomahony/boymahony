#!/usr/bin/python
import requests
import json

url = 'https://api.jcdecaux.com/vls/v1/stations'

params = {'apiKey': '50f272d1f5a2e9c3cdad61c200167195f2651655',
'contract': "Dublin"
}

response = requests.get(url,params=params)

low_availability = {}

print (response.status_code)
stations = response.json()
for station in stations:
    if station['available_bikes'] < 10:
        name = station['name']
        count = station['available_bikes']
        # print (station['name'], station['available_bikes'])
        low_availability[name] = count


print(low_availability)
with open('low_availability_stations.json', 'w') as f:
    json.dump(low_availability, f, indent=2, sort_keys=True)
