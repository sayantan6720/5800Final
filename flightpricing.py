import requests
import json

# Your API key should go here
api_key = 'sh428739766321522266746152871799'

# The data payload
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

# Headers
headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key
}

# The endpoint URL
url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'

# Make the POST request
response = requests.post(url, headers=headers, json=data)


# Check the response
if response.ok:
    # If response is OK, print the content
    print(response.json())
else:
    # If response is not OK, print the error
    print(f"Failed to retrieve data: {response.status_code}, {response.text}")
