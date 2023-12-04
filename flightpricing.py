import requests
import json

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'sh428739766321522266746152871799'
}


data = {
    "query": {
        "market": "US",
        "locale": "en-US",
        "currency": "USD",
        "queryLegs": [
            {
                "originPlaceId":

                    {

                        "iata": "IAD",
                    },
                "destinationPlaceId":
                    {
                        "iata": "JFK",
                    },
                "date":
                    {

                        "year": 2024,
                        "month": 4,
                        "day": 12

                    }
            }
        ],
    },
    "cabinClass": "CABIN_CLASS_ECONOMY",
    "adults": 2,
    "childrenAges": [],
    "includedCarrierIds": [],
    "excludedCarrierIds": [],
    "includedAgentsIds": [],
    "excludedAgentsIds": [],
    "includeSubsidiaryData": True,
    "nearbyAirports": True
}


response = requests.post(
    'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create',
    headers=headers,
    json=data
)

print(response, response.content)

