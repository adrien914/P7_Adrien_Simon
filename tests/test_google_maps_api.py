import json
from utils import google_maps_api
import requests


def test_google_maps_api(monkeypatch):
    """
    Mock for google maps api calls
    """
    results = {
          "address_components": [
             {
                "long_name": "Place Charles de Gaulle",
             },
          ],
          "geometry": {
             "location": {
                "lat": 48.8737917,
                "lng": 2.2950275
             },
          },
        }


    class MockResponse:
        def __init__(self, url, params):
            return

        def json(self):
            return {"results": results}

    monkeypatch.setattr(requests, 'get', MockResponse)
    assert google_maps_api.GoogleMapsApi().geolocate("Arc triomphe") == results

