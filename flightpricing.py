import requests
import json

api_key = 'sh428739766321522266746152871799'

data = {
    "query": {
        "market": "US",
        "locale": "en-US",
        "currency": "USD",
        "queryLegs": [
            {
                "originPlaceId": {"iata": "DCA"},
                "destinationPlaceId": {"iata": "JFK"},
                "date": {"year": 2023, "month": 12, "day": 12}
            }
        ],
    },
    "cabinClass": "CABIN_CLASS_ECONOMY",
    "adults": 1,
    "childrenAges": [],
    "includedCarrierIds": [],
    "excludedCarrierIds": [],
    "includedAgentsIds": [],
    "excludedAgentsIds": [],
    "includeSubsidiaryData": True,
    "nearbyAirports": True
}

headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'

response = requests.post(url, headers=headers, json=data)


if response.ok:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}, {response.text}")
