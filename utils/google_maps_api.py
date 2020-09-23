from decouple import config
import requests


class GoogleMapsApi:

    api_key = config('API_KEY')  # Get the api key from the .env file
    base_url = "https://maps.googleapis.com"

    def geolocate(self, sentence: str) -> dict:
        """
        This method calls the gelocalization google api to find a place from a sentence
        :param sentence: the sentence to send to the api
        :return: the result of the request
        """
        url = self.base_url + "/maps/api/geocode/json"
        params = {
            "key": self.api_key,
            "address": sentence + ",france",
        }
        result = requests.get(url, params).json().get("results", None)
        if not result:
            params["address"] = sentence
            result = requests.get(url, params).json().get("results", None)
        print(result)
        return result
